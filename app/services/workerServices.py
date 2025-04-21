from app.database import getDatabase, setDatabase
from app.database.workers import Worker, WorkerPosition, Cehove, TimePaper, TimePaperOperation
import pandas as pd

class WorkerServices:
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
                        timePaper.WorkerId,
                        operation.productionModelOperations.ПоръчкаNo,
                        operation.productionModelOperations.ОперацияNo,
                        operation.productionModelOperations.Операция,
                        operation.Pieces,
                        operation.WorkingTimeMinutes
                    ])
                    # if "workerId" not in returnedData.keys():
                    #     returnedData["workerId"] = [timePaper.WorkerId]
                    # else:
                    #     returnedData["workerId"].append(timePaper.WorkerId)
                    # if "orderNo" not in returnedData.keys():
                    #     returnedData["orderNo"] = [operation.productionModelOperations.ПоръчкаNo]
                    # else:
                    #     returnedData["orderNo"].append(operation.productionModelOperations.ПоръчкаNo)
                    # if "operationNo" not in returnedData.keys():
                    #     returnedData["operationNo"] = [operation.productionModelOperations.ОперацияNo]
                    # else:
                    #     returnedData["operationNo"].append(operation.productionModelOperations.ОперацияNo)
                    # if "operation" not in returnedData.keys():
                    #     returnedData["operation"] = [operation.productionModelOperations.Операция]
                    # else:
                    #     returnedData["operation"].append(operation.productionModelOperations.Операция)
                    # if "pieces" not in returnedData.keys():
                    #     returnedData["pieces"] = [operation.Pieces]
                    # else:
                    #     returnedData["pieces"].append(operation.Pieces)
                    # if "time" not in returnedData.keys():
                    #     returnedData["time"] = [operation.WorkingTimeMinutes]
                    # else:
                    #     returnedData["time"].append(operation.WorkingTimeMinutes)

            return returnedData
