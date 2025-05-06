from app.logger import logger
from app.database import getDatabase, setDatabase
from app.database.workers import Worker, TimePaper, TimePaperOperation, WorkingShift, HourlyPay, OvertimePay
from app.database.payment import PaymentPerMinute
from datetime import datetime

class WorkerServices:

    @staticmethod
    def getWorkerDataForPayments(workerId):
        with getDatabase() as session:
            worker = session.query(Worker).filter(Worker.Номер == workerId).first()
            if worker is not None:
                return {
                    'id': worker.Номер,
                    'firstName': worker.Име,
                    'lastName': worker.Фамилия,
                    'place': worker.cehove.Група,
                    'position': worker.workerPosition.Длъжност,
                }

    @staticmethod
    def getPaymentsDetailsForWorker(workerId, startDate, endDate):
        startDate = datetime.strptime('2025-01-10', '%Y-%m-%d').date()
        endDate = datetime.strptime('2025-02-10', '%Y-%m-%d').date()
        returnedData = {}
        with getDatabase() as session:
            timePapers = session.query(TimePaper).filter(TimePaper.WorkerId == workerId,
                                                            TimePaper.Date >= startDate,
                                                            TimePaper.Date <= endDate).all()
            for timePaper in timePapers:
                operationsData = {}
                orderCount = []
                operationsCount = []
                if timePaper.timePaperOperations:
                    for timePaperOperation in timePaper.timePaperOperations:
                        operationsData[timePaperOperation.id] = {
                            'order': timePaperOperation.productionModelOperations.ПоръчкаNo,
                            'operation': timePaperOperation.productionModelOperations.ОперацияNo,
                            'time': timePaperOperation.WorkingTimeMinutes,
                            'pieces': timePaperOperation.Pieces,
                        }
                        if timePaperOperation.productionModelOperations.ПоръчкаNo not in orderCount:
                            orderCount.append(timePaperOperation.productionModelOperations.ПоръчкаNo)

                        if timePaperOperation.productionModelOperations.ОперацияNo not in operationsCount:
                            operationsCount.append(timePaperOperation.productionModelOperations.ОперацияNo)

                returnedData[timePaper.id] = {
                    'date': timePaper.Date.strftime('%d.%m.%Y'),
                    'shift': timePaper.workingShifts.ShiftName,
                    'operations': operationsData,
                    'isHourly': timePaper.hourlyPays.Efficiency if timePaper.hourlyPays is not None else 0,
                    'totalTime': timePaper.TotalHours,
                    'totalPieces': timePaper.TotalPieces,
                    'ordersCount': len(orderCount),
                    'operationsCount': len(operationsCount),
                }
            return returnedData

    @staticmethod
    def getPaymentForMin():
        with getDatabase() as session:
            return session.query(PaymentPerMinute).order_by(PaymentPerMinute.id.desc()).first()


    @staticmethod
    def getInfoForPayments(workerId, startDate, endDate):
        returnedData = {}
        startDate = datetime.strptime('2025-01-10', '%Y-%m-%d').date()
        endDate = datetime.strptime('2025-02-10', '%Y-%m-%d').date()
        with getDatabase() as session:
            if workerId != '':
                timePapers = session.query(TimePaper).filter(TimePaper.WorkerId == int(workerId),
                                                             TimePaper.Date >= startDate,
                                                             TimePaper.Date <= endDate).all()

            else:
                timePapers = session.query(TimePaper).filter(TimePaper.Date >= startDate,
                                                             TimePaper.Date <= endDate).all()

            for timePaper in timePapers:
                if timePaper.WorkerId is not None:
                    key = f'{timePaper.WorkerId} : {timePaper.workers.Име} {timePaper.workers.Фамилия}'
                    data = {
                                'date': timePaper.Date.strftime('%d.%m.%Y'),
                                'shift': [timePaper.workingShifts.ShiftName,
                                          timePaper.workingShifts.id,
                                          timePaper.workingShifts.Efficiency]
                                if timePaper.workingShifts is not None else None,
                                'overtime': [timePaper.overtimePays.id,
                                             timePaper.overtimePays.Efficiency]
                                if timePaper.overtimePays is not None else None,
                                'hourly': [timePaper.hourlyPays.id,
                                           timePaper.hourlyPays.Efficiency]
                                if timePaper.hourlyPays is not None else None,
                                'totalPieces': timePaper.TotalPieces,
                                'totalTime': round(timePaper.TotalHours, 2),
                        }
                    if key not in returnedData.keys():
                        returnedData[key] = {timePaper.id: data}
                    else:
                        returnedData[key][timePaper.id] = data
            # for key in returnedData.keys():
            #     print(key)
            #     print(returnedData[key])
            return returnedData



    @staticmethod
    def updateWorkingShift(shiftId, data):
        with setDatabase() as session:
            shift = session.query(WorkingShift).get(shiftId)
            shift.ShiftName = data[0],
            shift.ShiftStart = data[1],
            shift.ShiftEnd = data[2],
            shift.BreakTime = data[3],
            shift.Efficency = data[4],
            session.commit()
            logger.info(f"Working shift updated: {shift.id}")
            return True

    @staticmethod
    def addWorkingShift(newShiftData):
        with setDatabase() as session:
            newShift = WorkingShift(
                ShiftName=newShiftData[0],
                StartTime=newShiftData[1],
                EndTime=newShiftData[2],
                BreakTime=newShiftData[3],
                Efficiency=newShiftData[4],
                UserUpdated=newShiftData[5]
            )
            session.add(newShift)
            session.commit()
            logger.info(f"New working shift added: {newShift.id}")
            return True

    @staticmethod
    def deleteWorkingShift(shiftId):
        with setDatabase() as session:
            shift = session.query(WorkingShift).get(shiftId)
            session.delete(shift)
            session.commit()
            logger.info(f"Working shift deleted: {shift.id}")
            return True

    @staticmethod
    def addNewTimePaperAndOperation(timePaperData):
        with setDatabase() as session:
            if timePaperData['IsHourlyPaid']:
                newHourlyPay = HourlyPay(
                    Start=timePaperData['IsHourlyPaid'][0],
                    End=timePaperData['IsHourlyPaid'][1],
                    Efficiency=timePaperData['IsHourlyPaid'][2],
                    UserUpdated=timePaperData['user']
                )
                session.add(newHourlyPay)
                session.flush()
                timePaperData['IsHourlyPaid'] = newHourlyPay.id

            if timePaperData['IsOvertime']:
                newOvertimePay = OvertimePay(
                    Start=timePaperData['IsOvertime'][0],
                    End=timePaperData['IsOvertime'][1],
                    Efficiency=timePaperData['IsOvertime'][2],
                    OvertimeRate=0,
                    UserUpdated=timePaperData['user']
                )
                session.add(newOvertimePay)
                session.flush()
                timePaperData['IsOvertime'] = newOvertimePay.id

            newTimePaper = TimePaper(
                Date=timePaperData['Date'],
                ShiftId=timePaperData['ShiftId'],
                IsHourlyPaid=timePaperData['IsHourlyPaid'],
                IsOvertime=timePaperData['IsOvertime'],
                WorkerId=timePaperData['WorkerId'],
                userCreated=timePaperData['user']
            )
            session.add(newTimePaper)
            session.flush()



            newTimePaperOperation = TimePaperOperation(
                TimePaperId=newTimePaper.id,
                OrderId=timePaperData['OrderId'],
                ModelOperationId=timePaperData['ModelOperationId'],
                Pieces=timePaperData['Pieces'],
                WorkingTimeMinutes=timePaperData['WorkingTimeMinutes']
            )
            session.add(newTimePaperOperation)
            session.flush()
            newTimePaper.TotalPieces += timePaperData['Pieces']
            newTimePaper.TotalHours = round(newTimePaper.TotalHours + timePaperData['WorkingTimeMinutes'], 2)

            newTimePaperOperation.productionModelOperations.ProducedPieces += newTimePaperOperation.Pieces

            session.commit()
            logger.info(f"New time paper and operation added: {timePaperData}")
            return newTimePaperOperation.id

    @staticmethod
    def updateTimePaperAndOperation(timePaperData):
        with setDatabase() as session:
            timePaper = session.query(TimePaper).get(timePaperData['TimePaperId'])
            newTimePaperOperation = TimePaperOperation(
                TimePaperId=timePaper.id,
                OrderId=timePaperData['OrderId'],
                ModelOperationId=timePaperData['ModelOperationId'],
                Pieces=timePaperData['Pieces'],
                WorkingTimeMinutes=timePaperData['WorkingTimeMinutes']
            )
            session.add(newTimePaperOperation)
            session.flush()
            timePaper.TotalPieces += timePaperData['Pieces']
            timePaper.TotalHours = round(timePaper.TotalHours + timePaperData['WorkingTimeMinutes'], 2)
            newTimePaperOperation.productionModelOperations.ProducedPieces += newTimePaperOperation.Pieces
            session.commit()
            logger.info(f"Time paper updated: {timePaperData}")
            return newTimePaperOperation.TimePaperId

    @staticmethod
    def getWorkers():
        with getDatabase() as session:
            data = []
            workers = session.query(Worker).order_by(Worker.Номер).all()
            for worker in workers:
                if worker.cehove and worker.workerPosition:
                    data.append([worker, worker.cehove.Група, worker.workerPosition.Длъжност])
            return data

    @staticmethod
    def getTimePapersForDate(date):
        returnedData = []
        with getDatabase() as session:
            timePapers = session.query(TimePaper).filter_by(Date=date).all()
            for timePaper in timePapers:
                for operation in timePaper.timePaperOperations:
                    returnedData.append([
                        timePaper.id,
                        timePaper.WorkerId,
                        operation.productionModelOperations.ПоръчкаNo,
                        operation.productionModelOperations.ОперацияNo,
                        operation.productionModelOperations.Операция,
                        operation.Pieces,
                        operation.WorkingTimeMinutes
                    ])
            return returnedData

    @staticmethod
    def getWorkingShiftsForEdit():
        with getDatabase() as session:
            return session.query(WorkingShift).order_by(WorkingShift.id).all()

    @staticmethod
    def getWorkingShifts():
        returnedData = {}
        with getDatabase() as session:
            shifts = session.query(WorkingShift).order_by(WorkingShift.id).all()
            for shift in shifts:
                returnedData[shift.ShiftName] = [
                    shift.id,
                    shift.StartTime,
                    shift.EndTime,
                ]
            return returnedData
