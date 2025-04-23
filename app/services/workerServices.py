from app.logger import logger
from app.database import getDatabase, setDatabase
from app.database.workers import Worker, TimePaper, TimePaperOperation, WorkingShift
import pandas as pd

class WorkerServices:

    @staticmethod
    def addNewTimePaperAndOperation(timePaperData):
        with setDatabase() as session:
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
            session.commit()
            logger.info(f"New time paper and operation added: {timePaperData}")
            return True

    @staticmethod
    def updateTimePaperAndOperation(timePaperData):
        with setDatabase() as session:
            newTimePaperOperation = TimePaperOperation(
                TimePaperId=timePaperData['TimePaperId'],
                OrderId=timePaperData['OrderId'],
                ModelOperationId=timePaperData['ModelOperationId'],
                Pieces=timePaperData['Pieces'],
                WorkingTimeMinutes=timePaperData['WorkingTimeMinutes']
            )
            session.add(newTimePaperOperation)
            session.commit()
            logger.info(f"Time paper updated: {timePaperData}")
            return True

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
