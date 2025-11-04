from sqlalchemy import func

from app.logger import logger
from app.database import getDatabase, setDatabase
from app.database.workers import Worker, TimePaper, TimePaperOperation, WorkingShift, HourlyPay, OvertimePay, Cehove,\
    PaymentType, WorkerPosition, OperationType
from app.database.payment import PaymentPerMinute, NightPaymentPerMinute, HolidaysPerYear, Holiday
from datetime import datetime


class WorkerServices:

    @staticmethod
    def addNewOperationType(data, rows):
        with setDatabase() as session:
            if data:
                newOperationType = OperationType(OperTypeID=rows + 1)
                for row, value in data.items():
                    setattr(newOperationType, row, value)
                session.add(newOperationType)
                session.commit()
                if newOperationType.OperTypeID:
                    logger.info(f'OperationType {newOperationType.OperTypeID} - {newOperationType.OperName} added')
                    return True
                else:
                    logger.error('Failed to add new OperationType')
                    return False
            else:
                logger.error('No data provided for new OperationType')
                return False

    @staticmethod
    def deleteSelectedOperationType(rowId):
        with setDatabase() as session:
            operationType = session.query(OperationType).filter_by(OperTypeID=rowId).first()
            if operationType:
                if not operationType.workerPositions and not operationType.operations:
                    session.delete(operationType)
                    session.commit()
                    logger.info(f'OperationType {rowId} deleted')
                    return 1
                else:
                    logger.error(f'OperationType {rowId} has workers associated, cannot delete')
                    return -1
            else:
                logger.error(f'OperationType {rowId} not found')
                return 0

    @staticmethod
    def addNewWorkerPosition(data, rows):
        with setDatabase() as session:
            if data:
                newPosition = WorkerPosition(ДлъжностКод=rows + 1)
                print(newPosition)
                for row, value in data.items():
                    # print(f'Adding new WorkerPosition: {row} - {value}')
                    setattr(newPosition, row, value)
                session.add(newPosition)
                session.commit()
                if newPosition.ДлъжностКод:
                    logger.info(f'WorkerPosition {newPosition.ДлъжностКод} - {newPosition.ДлъжностКод} added')
                    return True
                else:
                    logger.error('Failed to add new WorkerPosition')
                    return False
            else:
                logger.error('No data provided for new WorkerPosition')
                return False

    @staticmethod
    def deleteSelectedWorkerPosition(rowId):
        with setDatabase() as session:
            position = session.query(WorkerPosition).filter_by(ДлъжностКод=rowId).first()
            if position:
                if not position.workers or not position.operationType:
                    session.delete(position)
                    session.commit()
                    logger.info(f'WorkerPosition {rowId} deleted')
                    return 1
                else:
                    logger.error(f'WorkerPosition {rowId} has workers/opersType associated, cannot delete')
                    return -1
            else:
                logger.error(f'WorkerPosition {rowId} not found')
                return 0

    @staticmethod
    def addNewCehove(data):
        with setDatabase() as session:
            if data:
                newCeh = Cehove()
                for row, value in data.items():
                    # print(f'Adding new Cehove: {row} - {value}')
                    setattr(newCeh, row, value)
                session.add(newCeh)
                session.commit()
                if newCeh.id:
                    logger.info(f'Cehove {newCeh.id} - {newCeh.Група} added')
                    return True
                else:
                    logger.error('Failed to add new Cehove')
                    return False
            else:
                logger.error('No data provided for new Cehove')
                return False

    @staticmethod
    def deleteSelectedCehove(rowId):
        with setDatabase() as session:
            cehove = session.query(Cehove).filter_by(id=rowId).first()
            if cehove:
                if not cehove.workers:
                    session.delete(cehove)
                    session.commit()
                    logger.info(f'Cehove {rowId} deleted')
                    return 1
                else:
                    logger.error(f'Cehove {rowId} has workers associated, cannot delete')
                    return -1
            else:
                logger.error(f'Cehove {rowId} not found')
                return 0

    @staticmethod
    def getWorkersForCehove():
        returnedData = []
        with getDatabase() as session:
            workers = session.query(Worker).order_by(Worker.Номер).all()
            for worker in workers:
                returnedData.append(f'{worker.Номер}:  {worker.Име} {worker.Фамилия}')
            return returnedData

    @staticmethod
    def getOperationTypes():
        returnedData = []
        with getDatabase() as session:
            operationsTypes = session.query(OperationType).order_by(OperationType.OperTypeID).all()
            # print(operationsTypes)
            for operationType in operationsTypes:
                returnedData.append(f'{operationType.OperTypeID}:  {operationType.OperName}')
            return returnedData

    @staticmethod
    def deleteWorker(workerId):
        with setDatabase() as session:
            worker = session.query(Worker).filter_by(Номер=workerId).first()
            if worker:
                if not worker.timePapers:
                    session.delete(worker)
                    session.commit()
                    logger.info(f'Worker {workerId} deleted')
                    return True
                else:
                    logger.error(f'Worker {workerId} has time papers associated, cannot delete')
                    return False
            else:
                logger.error(f'Worker {workerId} not found')
                return False

    @staticmethod
    def setWorker(workerData):
        with setDatabase() as session:
            worker = session.query(Worker).filter_by(Номер=workerData['id']).first()
            if not worker:
                if not workerData['id']:
                    max_id = session.query(func.max(Worker.Номер)).scalar() or 0
                    worker = Worker(Номер=max_id + 1)
                else:
                    worker = Worker(Номер=workerData['id'])
                session.add(worker)
                session.flush()

            if worker:
                worker.Име = workerData['firstName'],
                worker.Презиме = workerData['middleName'],
                worker.Фамилия = workerData['lastName'],
                worker.Група = int(workerData['cehId']),
                worker.Длъжност = int(workerData['positionId']),
                worker.ЕГН = workerData['EGN'],
                worker.ДатаНаПостъпване = workerData['startDate'],
                worker.ДатаНаНапускане = workerData['endDate'],
                worker.СистемаЗаплащане = int(workerData['paymentTypeId']),
                worker.гр_с = workerData['town'],
                worker.Адрес = workerData['address'],
                worker.Телефон = workerData['workerPhone']
                session.commit()
                logger.info(f'Worker {worker.Номер}: {worker.Име} {worker.Фамилия} set')
                return True
            else:
                logger.error(f'Worker with ID {workerData["id"]} not found')
                return False

    @staticmethod
    def getCehove():
        returnedData = []
        with getDatabase() as session:
            cehove = session.query(Cehove).all()
            for ceh in cehove:
                returnedData.append(ceh.Група)
            return returnedData

    @staticmethod
    def getPositions():
        returnedData = []
        with getDatabase() as session:
            positions = session.query(WorkerPosition).all()
            for position in positions:
                returnedData.append(position.Длъжност)
            return returnedData

    @staticmethod
    def getPaymentTypes():
        returnedData = []
        with getDatabase() as session:
            paymentTypes = session.query(PaymentType).all()
            for paymentType in paymentTypes:
                returnedData.append(paymentType.Name)
            return returnedData

    @staticmethod
    def getWorkerInfo(workerId):
        with getDatabase() as session:
            return session.query(Worker).filter_by(Номер=workerId).first()

    @staticmethod
    def getWorkersInfo():
        returnedData = {}
        with getDatabase() as session:
            workers = session.query(Worker).order_by(Worker.Номер).all()
            for worker in workers:
                returnedData[worker.Номер] = {
                    'firstName': worker.Име,
                    'middleName': worker.Презиме,
                    'lastName': worker.Фамилия,
                    'ceh': worker.cehove.Група if worker.cehove else '-',
                    'position': worker.workerPosition.Длъжност if worker.workerPosition else '-',
                    'workerEGN': worker.ЕГН,
                    'startDate': worker.ДатаНаПостъпване.strftime('%d.%m-%Y') if worker.ДатаНаПостъпване else '-',
                    'endDate': worker.ДатаНаНапускане.strftime('%d.%m-%Y') if worker.ДатаНаНапускане else '-',
                    'paymentType': worker.paymentType.Name,
                    'town': worker.гр_с,
                    'address': worker.Адрес,
                    'phone': worker.Телефон,
                    'workerExpYears': worker.ТрудовСтажГодини if worker.ТрудовСтажГодини else 0,
                    'workerExpMonths': worker.ТрудовСтажМесеци if worker.ТрудовСтажМесеци else 0,
                    'workerExpDays': worker.ТрудовСтажДни if worker.ТрудовСтажДни else 0,
                    'workerExpStart': worker.ДатаНачалоТрудСтаж.strftime('%d.%m.%Y') if worker.ДатаНачалоТрудСтаж else '-',
                }
            return returnedData

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
        # startDate = datetime.strptime('2024-10-01', '%Y-%m-%d').date()
        # endDate = datetime.strptime('2024-11-01', '%Y-%m-%d').date()
        returnedData = {}
        currentYear = datetime.now().year
        with getDatabase() as session:
            holidaysList = WorkerServices.getHolidaysForYear(session, currentYear)
            timePapers = session.query(TimePaper).filter(TimePaper.WorkerId == workerId,
                                                            TimePaper.Date >= startDate,
                                                            TimePaper.Date <= endDate).all()
            for timePaper in timePapers:
                operationsData = {}
                orderCount = []
                operationsCount = []
                hourlyPayList = []
                overtimePayList = []
                if timePaper.timePaperOperations:
                    for timePaperOperation in timePaper.timePaperOperations:
                        operationsData[timePaperOperation.id] = {
                            'order': timePaperOperation.productionModelOperations.ПоръчкаNo,
                            'operation': timePaperOperation.productionModelOperations.ОперацияNo,
                            'time': timePaperOperation.WorkingTimeMinutes,
                            'pieces': timePaperOperation.Pieces,
                            'nightMins': timePaperOperation.NightMins,
                        }
                        if timePaperOperation.productionModelOperations.ПоръчкаNo not in orderCount:
                            orderCount.append(timePaperOperation.productionModelOperations.ПоръчкаNo)

                        if timePaperOperation.productionModelOperations.ОперацияNo not in operationsCount:
                            operationsCount.append(timePaperOperation.productionModelOperations.ОперацияNo)

                if timePaper.hourlyPays:
                    for hourlyPay in timePaper.hourlyPays:
                        hourlyPayList.append([hourlyPay.Efficiency, hourlyPay.HourlyRate,
                                              hourlyPay.id, hourlyPay.NightMins])

                if timePaper.overtimePays:
                    for overtimePay in timePaper.overtimePays:
                        overtimePayList.append([overtimePay.Efficiency, overtimePay.OvertimeRate,
                                                overtimePay.id, overtimePay.NightMins])

                if timePaper.Date in holidaysList:
                    paymentRatio = 2
                else:
                    paymentRatio = timePaper.PaymentRatio

                returnedData[timePaper.id] = {
                    'date': timePaper.Date.strftime('%d.%m.%Y'),
                    'shift': timePaper.workingShifts.ShiftName if timePaper.workingShifts else '-',
                    'operations': operationsData,
                    'hourly': hourlyPayList,
                    'overtime': overtimePayList,
                    'nightMins': timePaper.NightShiftMins,
                    'totalTime': timePaper.TotalHours,
                    'totalPieces': timePaper.TotalPieces,
                    'ordersCount': len(orderCount),
                    'operationsCount': len(operationsCount),
                    'paymentRatio': paymentRatio
                }
            return returnedData

    @staticmethod
    def getHolidaysForYear(session, year):
        holidays = None
        holidaysPerYear = session.query(HolidaysPerYear).filter_by(Year=year).first()
        if holidaysPerYear:
            holidays = session.query(Holiday).filter_by(HolidaysPerYearId=holidaysPerYear.id).all()
        if holidays:
            holidaysList = [holiday.HolidayDate for holiday in holidays]
        else:
            holidaysList = []
        return holidaysList

    @staticmethod
    def getPaymentsForMin():
        with getDatabase() as session:
            return session.query(PaymentPerMinute).order_by(PaymentPerMinute.id.asc()).all()

    @staticmethod
    def getPaymentForMin():
        with getDatabase() as session:
            return session.query(PaymentPerMinute).filter_by(Active=True).first()

    @staticmethod
    def getPaymentForNightMin():
        with getDatabase() as session:
            return session.query(NightPaymentPerMinute).filter_by(Active=True).first()

    @staticmethod
    def getInfoForPayments(startDate, endDate):
        returnedData = {}
        # startDate = datetime.strptime('2024-10-01', '%Y-%m-%d').date()
        # endDate = datetime.strptime('2024-11-01', '%Y-%m-%d').date()
        currentYear = datetime.now().year
        with getDatabase() as session:
            holidaysList = WorkerServices.getHolidaysForYear(session, currentYear)
            timePapers = session.query(TimePaper).filter(TimePaper.Date >= startDate,
                                                         TimePaper.Date <= endDate).all()

            for timePaper in timePapers:
                if timePaper.WorkerId is not None:
                    key = f'{timePaper.WorkerId} : {timePaper.workers.Име} {timePaper.workers.Фамилия}'

                    overtimeAndHourly = WorkerServices.checkOvertimeAndHourly(timePaper)

                    if timePaper.Date in holidaysList:
                        paymentRatio = 2
                    else:
                        paymentRatio = timePaper.PaymentRatio

                    data = {
                                'date': timePaper.Date.strftime('%d.%m.%Y'),
                                'shift': [timePaper.workingShifts.ShiftName,
                                          timePaper.workingShifts.id,
                                          timePaper.workingShifts.Efficiency,
                                          timePaper.workingShifts.StartTime,
                                          timePaper.workingShifts.EndTime]
                                if timePaper.workingShifts is not None else None,
                                'overtime': overtimeAndHourly[0],
                                'hourly': overtimeAndHourly[1],
                                'nightMins': timePaper.NightShiftMins,
                                'totalPieces': timePaper.TotalPieces,
                                'totalTime': round(timePaper.TotalHours, 2),
                                'paymentRatio': paymentRatio
                        }
                    if key not in returnedData.keys():
                        returnedData[key] = {timePaper.id: data}
                    else:
                        returnedData[key][timePaper.id] = data
            return returnedData

    # @staticmethod
    # def getPaymentRation(timePaper):
    #     with getDatabase() as session:
    #         if timePaper.WeekDay and timePaper.WeekDay > 5:
    #             return 1.75
    #         holidaysForYear = session.query(HolidaysPerYear).filter_by(
    #             Year=int(datetime.strftime(datetime.now(), '%Y'))).first()
    #         for haliday in holidaysForYear.holidays:
    #             if timePaper.Date == haliday.HolidayDate:
    #                 return 2
    #         return 1

    @staticmethod
    def checkOvertimeAndHourly(timePaper):
        overtime = {}
        hourly = {}
        if timePaper.overtimePays:
            for overtimePay in timePaper.overtimePays:
                overtime[overtimePay.id] = [overtimePay.Efficiency, overtimePay.OvertimeRate, overtimePay.NightMins]

        if timePaper.hourlyPays:
            for hourlyPay in timePaper.hourlyPays:
                hourly[hourlyPay.id] = [hourlyPay.Efficiency, hourlyPay.HourlyRate, hourlyPay.NightMins]

        return overtime, hourly

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
            if not shift.timePapers:
                session.delete(shift)
                session.commit()
                logger.info(f"Working shift deleted: {shift.id}")
                return True
            else:
                logger.error(f"Cannot delete working shift with time papers: {shift.id}")
                return False

    @staticmethod
    def deleteTimePapers(slectedIds):
        with setDatabase() as session:
            timePaperId = None
            for timePaperOperationId in slectedIds:
                if timePaperOperationId.split('_')[1] == 'operation':
                    timePaperOperation = session.query(TimePaperOperation).get(int(timePaperOperationId.split('_')[0]))
                    if timePaperOperation is not None:
                        nightMins = timePaperOperation.timePaper.NightShiftMins
                        timePaperId = timePaperOperation.TimePaperId

                        timePaperOperation.timePaper.TotalPieces -= timePaperOperation.Pieces
                        timePaperOperation.timePaper.TotalHours -= timePaperOperation.WorkingTimeMinutes
                        timePaperOperation.timePaper.TotalHours = round(timePaperOperation.timePaper.TotalHours, 2)

                        timePaperOperation.productionModelOperations.ProducedPieces -= timePaperOperation.Pieces

                        nightMins -= timePaperOperation.NightMins
                        timePaperOperation.timePaper.NightShiftMins = round(nightMins, 2)

                        session.delete(timePaperOperation)
                        logger.info(f"Time paper operation deleted: {timePaperOperationId}")
                elif timePaperOperationId.split('_')[1] == 'hourlyPay':
                    timePaperHourlyPay = session.query(HourlyPay).get(int(timePaperOperationId.split('_')[0]))
                    if timePaperHourlyPay is not None:
                        timePaperId = timePaperHourlyPay.TimePaperId
                        session.delete(timePaperHourlyPay)
                        logger.info(f"Time paper hourly pay deleted: {timePaperOperationId}")
                else:
                    timePaperOvertimePay = session.query(OvertimePay).get(int(timePaperOperationId.split('_')[0]))
                    if timePaperOvertimePay is not None:
                        timePaperId = timePaperOvertimePay.TimePaperId
                        session.delete(timePaperOvertimePay)
                        logger.info(f"Time paper overtime pay deleted: {timePaperOperationId}")
            session.flush()
            if timePaperId:
                timePaper = session.query(TimePaper).get(timePaperId)
                if not timePaper.timePaperOperations and not timePaper.overtimePays and not timePaper.hourlyPays:
                    session.delete(timePaper)
                    logger.info(f"Time paper deleted: {timePaper.id}")
            session.commit()
            return True

    @staticmethod
    def updateTimePaperPieces(operId, newPieces, newTime, nightShiftMins):
        with setDatabase() as session:
            timePaperOperation = session.query(TimePaperOperation).get(operId)
            if timePaperOperation is not None:
                hourlyNightMins = WorkerServices.getNightMinsFromHourly(
                    timePaperOperation.timePaper.id, session
                )
                nightShiftMins -= hourlyNightMins
                totalTimePaperTime = timePaperOperation.timePaper.TotalHours
                totalTimePaperPieces = timePaperOperation.timePaper.TotalPieces
                totalNightMins = timePaperOperation.timePaper.NightShiftMins

                totalTimePaperTime -= timePaperOperation.WorkingTimeMinutes
                totalTimePaperPieces -= timePaperOperation.Pieces

                if timePaperOperation.NightMins > 0:
                    totalNightMins -= timePaperOperation.NightMins

                if nightShiftMins > 0:
                    if nightShiftMins < totalNightMins + newTime:
                        timePaperOperation.NightMins = newTime - ((totalNightMins + newTime) - nightShiftMins)
                    else:
                        timePaperOperation.NightMins = newTime

                totalNightMins += timePaperOperation.NightMins

                timePaperOperation.Pieces = newPieces
                timePaperOperation.WorkingTimeMinutes = round(newTime, 2)

                totalTimePaperPieces += newPieces
                totalTimePaperTime += newTime
                totalTimePaperTime = round(totalTimePaperTime, 2)

                timePaperOperation.timePaper.TotalHours = totalTimePaperTime
                timePaperOperation.timePaper.TotalPieces = totalTimePaperPieces
                timePaperOperation.timePaper.NightShiftMins = round(totalNightMins, 2)

                session.commit()
                logger.info(f"Time paper operation updated: {operId} New pieces: {newPieces}, New time: {newTime}")
                return True
            else:
                logger.error(f"Unable to update time paper operation: {operId}")
                return False

    @staticmethod
    def getNightMinsFromHourly(timePaperId, session):
        totalNightMins = 0

        hourly = session.query(HourlyPay).filter_by(TimePaperId=timePaperId).all()

        if hourly:
            for hourlyPay in hourly:
                totalNightMins += hourlyPay.NightMins

        return totalNightMins


    @staticmethod
    def addNewTimePaperAndOperation(timePaperData):
        with setDatabase() as session:
            if timePaperData['WeekDay'] and timePaperData['WeekDay'] > 5:
                paymentRatio = 1.75
            else:
                paymentRatio = 1

            newTimePaper = TimePaper(
                Date=timePaperData['Date'],
                WeekDay=timePaperData['WeekDay'],
                PaymentRatio=paymentRatio,
                ShiftId=timePaperData['ShiftId'],
                WorkerId=timePaperData['WorkerId'],
                userCreated=timePaperData['user']
                # NightShiftMins=timePaperData['nightMins']
            )
            session.add(newTimePaper)
            session.commit()
            if WorkerServices.addTimePaperDetails(session, newTimePaper, timePaperData):
                session.commit()
                logger.info(f"New time paper and operation added: {timePaperData}")
                return newTimePaper.id
            else:
                logger.error(f"Unable to add new time paper and operation: {timePaperData}")
                return None

    @staticmethod
    def updateTimePaperAndOperation(timePaperData):
        with setDatabase() as session:
            timePaper = session.query(TimePaper).get(timePaperData['TimePaperId'])
            if WorkerServices.addTimePaperDetails(session, timePaper, timePaperData):
                session.commit()
                logger.info(f"Time paper updated: {timePaperData}")
                return True
            else:
                logger.error(f"Time paper update failed: {timePaperData}")
                return False
            # return newTimePaperOperation.TimePaperId

    @staticmethod
    def addTimePaperDetails(session, timePaper, timePaperData):

        # if timePaperData['nightMins'] > 0:
        #     timePaper.NightShiftMins += timePaperData['nightMins']
        currentNightMin = 0
        if timePaper.hourlyPays:
            for hourlyPay in timePaper.hourlyPays:
                currentNightMin += hourlyPay.NightMins
        currentNightMin += timePaper.NightShiftMins
        currentShiftNightMins = timePaperData['currentShiftNightMins']
        nightMins = timePaperData['nightMins']

        if timePaperData['ModelOperationId']:
            operationNightMin = 0
            if currentNightMin < nightMins > 0:
                if nightMins - currentNightMin >= timePaperData['WorkingTimeMinutes']:
                    operationNightMin = timePaperData['WorkingTimeMinutes']
                else:
                    operationNightMin = nightMins - currentNightMin
            newTimePaperOperation = TimePaperOperation(
                TimePaperId=timePaper.id,
                OrderId=timePaperData['OrderId'],
                ModelOperationId=timePaperData['ModelOperationId'],
                Pieces=timePaperData['Pieces'],
                WorkingTimeMinutes=timePaperData['WorkingTimeMinutes'],
                NightMins=round(operationNightMin, 2)
            )
            session.add(newTimePaperOperation)
            session.flush()
            timePaper.TotalPieces += timePaperData['Pieces']
            timePaper.TotalHours = round(timePaper.TotalHours + timePaperData['WorkingTimeMinutes'], 2)
            timePaper.NightShiftMins = round(timePaper.NightShiftMins + operationNightMin, 2)
            return True

        elif timePaperData['IsHourlyPaid']:
            hourlyNightMin = 0
            if currentNightMin < currentShiftNightMins and nightMins > 0:
                if currentShiftNightMins - currentNightMin >= nightMins:
                    hourlyNightMin = nightMins
                else:
                    hourlyNightMin = currentShiftNightMins - currentNightMin
            newHourlyPay = HourlyPay(
                TimePaperId=timePaper.id,
                Start=timePaperData['IsHourlyPaid'][0],
                End=timePaperData['IsHourlyPaid'][1],
                Efficiency=timePaperData['IsHourlyPaid'][2],
                NightMins=round(hourlyNightMin, 2),
                UserUpdated=timePaperData['user']
            )
            session.add(newHourlyPay)
            session.flush()
            return True

        elif timePaperData['IsOvertime']:
            if timePaperData['nightMins'] > 0:
                overtimeNightMin = timePaperData['nightMins']
            else:
                overtimeNightMin = 0
            newOvertimePay = OvertimePay(
                TimePaperId=timePaper.id,
                Start=timePaperData['IsOvertime'][0],
                End=timePaperData['IsOvertime'][1],
                Efficiency=timePaperData['IsOvertime'][2],
                NightMins=overtimeNightMin,
                OvertimeRate=1.5,
                UserUpdated=timePaperData['user']
            )
            session.add(newOvertimePay)
            session.flush()
            return True
        else:
            return False

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
    def getExistingTimePaperShift(timePaperId):
        with getDatabase() as session:
            timePaper = session.query(TimePaper).get(timePaperId)
            if timePaper:
                returnedShiftInfo = [timePaper.workingShifts.ShiftName,
                                     timePaper.workingShifts.StartTime,
                                     timePaper.workingShifts.EndTime]
                # returnedShiftInfo = timePaper.workingShifts.ShiftName
                return returnedShiftInfo
            else:
                return None

    @staticmethod
    def getTimePapersForDate(date, workerId, showAll=False):
        returnedData = []
        timePapers = []
        with getDatabase() as session:
            if workerId:
                timePapers = session.query(TimePaper).filter_by(Date=date, WorkerId=workerId).all()
            if showAll:
                timePapers = session.query(TimePaper).filter_by(Date=date).all()
            for timePaper in timePapers:

                if timePaper.hourlyPays:
                    for hourlyPay in timePaper.hourlyPays:
                        hourlyTime = hourlyPay.Efficiency
                        orderId = 'Почасова работа'
                        horlyItem = [
                            timePaper.id,
                            timePaper.WorkerId,
                            orderId,
                            '',
                            '',
                            0,
                            0,
                            -1,
                            hourlyTime,
                            hourlyPay.id
                        ]
                        returnedData.append(horlyItem)
                if timePaper.overtimePays:
                    for overtimePay in timePaper.overtimePays:
                        overtimeTime = overtimePay.Efficiency
                        orderId = 'Извънредна работа'
                        overtimeItem = [
                            timePaper.id,
                            timePaper.WorkerId,
                            orderId,
                            '',
                            '',
                            0,
                            0,
                            -1,
                            overtimeTime,
                            overtimePay.id
                        ]
                        returnedData.append(overtimeItem)

                for operation in timePaper.timePaperOperations:
                    returnedData.append([
                        timePaper.id,
                        timePaper.WorkerId,
                        operation.productionModelOperations.ПоръчкаNo,
                        operation.productionModelOperations.ОперацияNo,
                        operation.productionModelOperations.Операция,
                        operation.Pieces,
                        operation.WorkingTimeMinutes,
                        operation.id,
                        operation.productionModelOperations.OrderId,
                        operation.productionModelOperations.id
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
