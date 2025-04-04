from app.database import getDatabase, setDatabase
from app.database.models import VidObleklo, Client, ProductionModel, Machine, Yarn, ProducedPiecesForModel
from app.database.operations import DefaultOperForVidObleklo, ProductionModelOperations


class ModelService:

    @staticmethod
    def getDfaultOperations(vidOblekloId):
        with getDatabase() as session:
            return session.query(VidObleklo).filter_by(OblekloVid=vidOblekloId).first().defaultOperForVidOblekla

    @staticmethod
    def getClients():
        with getDatabase() as session:
            return session.query(Client).all()

    @staticmethod
    def getAllModels():
        with getDatabase() as session:
            return session.query(ProductionModel).all()

    @staticmethod
    def addNewModel(newModel, operations):
        with setDatabase() as session:
            newModelToAdd = ProductionModel(
                ПоръчкаNo=newModel['orderNo'],
                Descr=newModel['descr'],
                Actual=newModel['actual'],
                ClientID=newModel['clientId'],
                MachineId=newModel['machineId'],
                Fain=newModel['fain'],
                WearType=newModel['wearType'],
                YarnType=newModel['yarnId'],
                Броя=newModel['pieces'],
                DateCreated=newModel['dateCreated'],
                TargetDate=newModel['targetDate'],
                UserCreated=newModel['userCreated']
            )
            session.add(newModelToAdd)
            session.flush()

            if newModelToAdd.Броя:

                modelPieces = ProducedPiecesForModel(
                    orderNo=newModelToAdd.id,
                    ПоръчкаNo=newModelToAdd.ПоръчкаNo,
                    OrderPieces=newModelToAdd.Броя,
                    Produced=0,
                    Rest=newModelToAdd.Броя
                )
                session.add(modelPieces)
                session.flush()

            for operation, values in operations.items():
                session.add(ProductionModelOperations(
                    OrderId=newModelToAdd.id,
                    ПоръчкаNo=newModelToAdd.ПоръчкаNo,
                    ОперацияNo=operation,
                    Операция=values[0],
                    TimeForOper=values[1],
                    Razcenka=0,  # Here will be added price for operation,
                    LastUpdated=newModel['dateCreated'],
                    UpdatedBy=newModel['userCreated']
                ))
            session.commit()
            return newModelToAdd.ПоръчкаNo

    @staticmethod
    def getModelsForClient(clientId):
        with getDatabase() as session:
            return session.query(ProductionModel).filter_by(ClientID=clientId).all()

    @staticmethod
    def getModelInfo(modelId):
        with getDatabase() as session:
            model = session.query(ProductionModel).filter_by(id=modelId).first()
            modelFine = model.Fain if model else None
            modelMachine = f'{model.MachineId}: {model.machine.MachineType}' if model.machine else None
            modelYarn = f'{model.YarnType}: {model.yarn.ПреждаТип}' if model.yarn else None
            modelObleklo = f'{model.WearType}: {model.vidOblekla.OblekloName}'
            return [modelFine, modelMachine, modelYarn, modelObleklo]

    @staticmethod
    def getAllModelTypes():
        with getDatabase() as session:
            return session.query(VidObleklo).order_by(VidObleklo.OblekloVid.asc()).all()

    @staticmethod
    def getVidObjekla():
        returnedData = {}
        with getDatabase() as session:
            vidObjekla = session.query(VidObleklo).order_by(VidObleklo.OblekloVid.asc()).all()
            for vidObleklo in vidObjekla:
                returnedData[f'{vidObleklo.OblekloVid}: {vidObleklo.OblekloName}'] = vidObleklo.OblekloVid
            return returnedData

    @staticmethod
    def getMachines():
        returnedData = {}
        with getDatabase() as session:
            machines = session.query(Machine).order_by(Machine.MachineId.asc()).all()
            for machine in machines:
                returnedData[f'{machine.MachineId}: {machine.MachineType}'] = [machine.MachineId, machine.MachineFine]
            return returnedData

    @staticmethod
    def getYarns():
        returnedData = {}
        with getDatabase() as session:
            yarns = session.query(Yarn).order_by(Yarn.YarnID.asc()).all()
            for yarn in yarns:
                returnedData[f'{yarn.YarnID}: {yarn.ПреждаТип}'] = [yarn.YarnID, yarn.Състав]
            return returnedData

    @staticmethod
    def getOperationsForModelType(vidObleklo):
        with getDatabase() as session:
            operations = session.query(DefaultOperForVidObleklo).filter_by(OblekloVid=vidObleklo).all()
            if operations:
                return operations

    @staticmethod
    def saveOperationsForModelType(modelTypeId, operations):
        with setDatabase() as session:
            if session.query(DefaultOperForVidObleklo).filter_by(OblekloVid=modelTypeId).all():
                session.query(DefaultOperForVidObleklo).filter_by(OblekloVid=modelTypeId).delete()
            for index, operation in enumerate(operations):
                newOperation = DefaultOperForVidObleklo(OblekloVid=modelTypeId,
                                                        ОперацияNo=operation[0],
                                                        defaultTime=float(operation[2]))
                session.add(newOperation)
            return True
