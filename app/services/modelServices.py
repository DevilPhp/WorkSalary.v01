from sqlalchemy import func

from app.logger import logger
from app.database import getDatabase, setDatabase
from app.database.models import VidObleklo, Client, ProductionModel, Machine, Yarn, ProducedPiecesForModel
from app.database.operations import DefaultOperForVidObleklo, ProductionModelOperations


class ModelService:

    @staticmethod
    def deleteDefaultModelType(modelTypeId):
        with setDatabase() as session:
            modelType = session.query(VidObleklo).filter_by(OblekloVid=modelTypeId).first()
            if modelType and not modelType.productionModel:
                if modelType.defaultOperForVidOblekla:
                    for operation in modelType.defaultOperForVidOblekla:
                        session.delete(operation)
                        logger.info(f"Default operation {operation.id} deleted successfully.")
                session.delete(modelType)
                session.commit()
                logger.info(f"Default model type {modelTypeId} - {modelType.OblekloName} deleted successfully.")
                return True
            else:
                logger.error(f"Failed to delete default model type {modelTypeId}.")
                return False

    @staticmethod
    def addNewDefaultModelType(name):
        with setDatabase() as session:
            maxId = session.query(func.max(VidObleklo.OblekloVid)).scalar() or 0
            newModelType = VidObleklo(
                OblekloVid=maxId + 1,
                OblekloName=name
            )
            session.add(newModelType)
            session.commit()
            if newModelType:
                logger.info(f"New default model type {newModelType.OblekloVid} - {name} added successfully.")
                return True
            else:
                logger.error(f"Failed to add new default model type '{name}'.")
                return False

    @staticmethod
    def getModelOperations(modelId):
        with getDatabase() as session:
            model = session.query(ProductionModel).filter_by(id=modelId).first()
            return model.productionModelOperations, model.Броя

    @staticmethod
    def getClientsAndModels():
        with getDatabase() as session:
            return session.query(Client, ProductionModel).join(ProductionModel).all()

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

            # if newModelToAdd.Броя:
            #
            #     modelPieces = ProducedPiecesForModel(
            #         orderNo=newModelToAdd.id,
            #         ПоръчкаNo=newModelToAdd.ПоръчкаNo,
            #         OrderPieces=newModelToAdd.Броя,
            #         Produced=0,
            #         Rest=newModelToAdd.Броя
            #     )
            #     session.add(modelPieces)
            #     session.flush()

            for operation, values in operations.items():
                session.add(ProductionModelOperations(
                    OrderId=newModelToAdd.id,
                    ПоръчкаNo=newModelToAdd.ПоръчкаNo,
                    ОперацияNo=operation,
                    Операция=values[0],
                    TimeForOper=values[1],
                    ProducedPieces=0,
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
            modelMachine = f'{model.MachineId}: {model.machine.MachineType} :  {model.machine.MachineFine}E' \
                if model.machine else None
            modelYarn = f'{model.YarnType}: {model.yarn.ПреждаТип} :  {model.yarn.Състав}' if model.yarn else None
            modelObleklo = f'{model.WearType}: {model.vidOblekla.OblekloName}'
            modelPieces = model.Броя if model else 0
            return [modelFine, modelMachine, modelYarn, modelObleklo, modelPieces]

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
                logger.info(f"All operations for model type {modelTypeId} deleted successfully.")

            if not operations:
                logger.info(f"No operations provided for model type {modelTypeId}.")
                return True
            for index, operation in enumerate(operations):
                newOperation = DefaultOperForVidObleklo(OblekloVid=modelTypeId,
                                                        ОперацияNo=operation[0],
                                                        defaultTime=float(operation[2]))
                session.add(newOperation)
                logger.info(f"Operation {operation[0]} for model type {modelTypeId} added successfully.")
            session.commit()
            logger.info(f"Operations for model type {modelTypeId} saved successfully.")

            return True
