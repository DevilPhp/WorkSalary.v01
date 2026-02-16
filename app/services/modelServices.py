import requests
from sqlalchemy import func

from app.logger import logger
from app.database import getDatabase, setDatabase
from app.database.models import VidObleklo, Client, ProductionModel, Machine, Yarn, ProducedPiecesForModel
from app.database.operations import DefaultOperForVidObleklo, ProductionModelOperations
from app.utils.appUtils import handle_api_connection
from config import API_SERVER


class ModelService:

    @staticmethod
    @handle_api_connection
    def addNewClient(data, rows):
        if data:
            response = requests.post(f'{API_SERVER}/model/add_client',
                                     json={'rows': rows, 'data': data}).json()
            if response['status'] == 'success':
                if response['data'] == 1:
                    logger.info(f'Client {data["Клиент"]} added')
                    return 1
                elif response['data'] == -1:
                    logger.error(f'Client with name {data["Клиент"]} already exists')
                    return -1
            else:
                logger.error('Failed to add new Client')
                return 0
        else:
            logger.error('No data provided for new Client')
            return 0

    @staticmethod
    @handle_api_connection
    def deleteClient(rowId, name):
        response = requests.post(f'{API_SERVER}/model/delete_client', json={'rowId': rowId, 'name': name}).json()
        if response['status'] =='success':
            if response['result'] == 1:
                logger.info(f"Client {rowId} - {name} deleted successfully.")
                return 1
            elif response['result'] == -1:
                logger.error(f"Failed to delete Client {rowId}. Client is linked to a prodModel.")
                return -1
            else:
                logger.error(f"Failed to delete Client {rowId}.")
                return 0
        else:
            logger.error('Failed to delete Client')
            return 0

    @staticmethod
    @handle_api_connection
    def addNewMachine(data, rows):
        if data:
            response = requests.post(f'{API_SERVER}/model/add_machine_type',
                                     json={'rows': rows, 'data': data}).json()
            if response['status'] == 'success':
                logger.info(f'MachineType {response["data"][0]} - {response["data"][1]} added')
                return True
            else:
                logger.error('Failed to add new MachineType')
                return False
        else:
            logger.error('No data provided for new MachineType')
            return False

    @staticmethod
    @handle_api_connection
    def deleteSelectedMachine(rowId):
        response = requests.post(f'{API_SERVER}/model/delete_machine_type', json={'rowId': rowId}).json()
        if response['status'] == 'success':
            if response['result'] == 1:
                logger.info(f"MachineType {rowId} deleted successfully.")
                return 1
            elif response['result'] == -1:
                logger.error(f"Failed to delete MachineType {rowId}.  Machine is linked to a Production Model.")
                return -1
            else:
                logger.error(f"Failed to delete MachineType {rowId}.")
                return 0
        else:
            logger.error('Failed to delete MachineType')
            return 0

    @staticmethod
    @handle_api_connection
    def addNewYarn(data, rows):
        if data:
            response = requests.post(f'{API_SERVER}/model/add_yarn',
                                     json={'rows': rows, 'data': data}).json()
            if response['status'] == 'success':
                logger.info(f'YarnType {response["data"][0]} - {response["data"][1]} - {response["data"][2]} added')
                return True
            else:
                logger.error('Failed to add new YarnType')
                return False
        else:
            logger.error('No data provided for new YarnType')
            return False

    @staticmethod
    @handle_api_connection
    def deleteSelectedYarn(rowId):
        response = requests.post(f'{API_SERVER}/model/delete_yarn', json={'rowId': rowId}).json()
        if response['status'] == 'success':
            if response['result'] == 1:
                logger.info(f"YarnType {rowId} deleted successfully.")
                return 1
            elif response['result'] == -1:
                logger.error(f"Failed to delete YarnType {rowId}.  Yarn is linked to a Production Model.")
                return -1
            else:
                logger.error(f"Failed to delete YarnType {rowId}.")
                return 0
        else:
            logger.error('Failed to delete YarnType')
            return 0

    @staticmethod
    @handle_api_connection
    def deleteDefaultModelType(modelTypeId):
        response = requests.post(f'{API_SERVER}/model/delete_default_model_type',
                                 json={'modelTypeId': modelTypeId}).json()
        if response['status'] =='success':
            logger.info(f"Default model type {modelTypeId} - {response['OblekloName']} deleted successfully.")
            return True
        else:
            logger.error(f"Failed to delete default model type {modelTypeId}.")
            return False

    @staticmethod
    @handle_api_connection
    def addNewDefaultModelType(name):
        responce = requests.post(f'{API_SERVER}/model/add_default_model_type',
                                 json={'name': name}).json()
        if responce['status'] =='success':
            logger.info(f"New default model type {name} added successfully.")
            return True
        else:
            logger.error(f"Failed to add new default model type '{name}'.")
            return False

    @staticmethod
    @handle_api_connection
    def getModelOperations(modelId):
        response = requests.get(f'{API_SERVER}/model/get_model_operations/{modelId}').json()
        if response['status'] =='success':
            # print(response['data'])
            return response['data']
        else:
            logger.error(f'Failed to get model {modelId} operations')
            return None

    @staticmethod
    @handle_api_connection
    def getClientsAndModels():
        response = requests.get(f'{API_SERVER}/model/get_clients_and_models').json()
        if response['status'] =='success':
            return response['data']
        else:
            logger.error('Failed to get clients and models')
            return None


    @staticmethod
    @handle_api_connection
    def getDfaultOperations(vidOblekloId):
        response = requests.get(f'{API_SERVER}/model/get_default_operations/{vidOblekloId}').json()
        if response['status'] =='success':
            return response['data']
        else:
            logger.error(f'Failed to get default operations for {vidOblekloId}')
            return None

    @staticmethod
    @handle_api_connection
    def getClients():
        response = requests.get(f'{API_SERVER}/model/get_clients').json()
        if response['status'] =='success':
            return response['data']
        else:
            logger.error('Failed to get clients')
            return None

        # with getDatabase() as session:
        #     return session.query(Client).all()

    # @staticmethod
    # @handle_api_connection
    # def getAllModels():
    #     response = requests.get(f'{API_SERVER}/model/get_all_models').json()
    #     if response['status'] =='success':
    #         return response['data']
    #     else:
    #         logger.error('Failed to get all models')
    #         return None
        #
        # with getDatabase() as session:
        #     return session.query(ProductionModel).all()

    @staticmethod
    @handle_api_connection
    def getForModelsGroups():
        response = requests.get(f'{API_SERVER}/model/get_for_models_groups').json()
        if response['status'] == 'success':
            return response['modelsDict']
        else:
            logger.error('Failed to get models groups')
            return None
        # with getDatabase() as session:
        #     models = session.query(ProductionModel).all()
        #     modelsDict = []
        #     for model in models:
        #         if model.Actual:
        #             modelsDict.append(f"{model.id} - {model.ПоръчкаNo}")
        #     return modelsDict

    @staticmethod
    # @handle_api_connection
    def checkIfOperationsCanBeDeleted(model, operations, removedOperations):
        print(operations)
    #     response = requests.post(f'{API_SERVER}/model/check_if_operations_can_be_deleted',
    #                              json={'modelId': model['orderNo'], 'operations': operations}).json()
    #     if response['status'] =='success':
    #         return response['updatedOperations']
    #     else:
    #         logger.error(f'Failed to check if operations can be deleted for {model["orderNo"]}')
    #         return None

        updatedOperations = []
        with getDatabase() as session:
            dbOperation = session.query(ProductionModelOperations).filter_by(OrderId=model['orderNo']).all()
            for operation in dbOperation:
                if operation.ОперацияNo in removedOperations and operation.timePaperOperations:
                    updatedOperations.append(str(operation.ОперацияNo))
            return updatedOperations

    @staticmethod
    @handle_api_connection
    def updateModel(model, operations):
        response = requests.post(f'{API_SERVER}/model/update_model',
                                 json={'modelId': model, 'operations': operations}).json()
        if response['status'] =='success':
            logger.info(f'Model {model["orderNo"]} updated successfully')
            return True
        else:
            logger.error(f'Failed to update model {model["orderNo"]}')
            return False
        #
        # with setDatabase() as session:
        #     operationsDict = {}
        #     modelToUpdate = session.query(ProductionModel).filter_by(id=model['orderNo']).first()
        #     if modelToUpdate:
        #         modelToUpdate.Descr = model['descr']
        #         modelToUpdate.MachineId = model['machineId']
        #         modelToUpdate.Fain = model['fain']
        #         modelToUpdate.WearType = model['wearType']
        #         modelToUpdate.YarnType = model['yarnId']
        #         modelToUpdate.Броя = model['pieces']
        #         modelToUpdate.Actual = model['actual']
        #
        #         existingOperations = session.query(ProductionModelOperations).filter_by(OrderId=model['orderNo']).all()
        #
        #         for existingOperation in existingOperations:
        #             operationsDict[existingOperation.ОперацияNo] = existingOperation
        #             if existingOperation.ОперацияNo not in operations.keys():
        #                 if not existingOperation.timePaperOperations:
        #                     session.delete(existingOperation)
        #                     logger.info(f"Operation {existingOperation.ОперацияNo} deleted from {model['orderNo']}.")
        #
        #         for operation, values in operations.items():
        #             if operation in operationsDict.keys():
        #                 operationsDict[operation].Операция = values[0]
        #                 operationsDict[operation].TimeForOper = values[1]
        #             else:
        #                 session.add(ProductionModelOperations(
        #                     OrderId=modelToUpdate.id,
        #                     ПоръчкаNo=modelToUpdate.ПоръчкаNo,
        #                     ОперацияNo=operation,
        #                     Операция=values[0],
        #                     TimeForOper=values[1],
        #                     ProducedPieces=0,
        #                     Razcenka=0,  # Here will be added price for operation,
        #                     LastUpdated=model['dateCreated'],
        #                     UpdatedBy=model['userCreated']
        #                 ))
        #
        #         session.commit()
        #         logger.info(f"Model {modelToUpdate.id} updated successfully.")
        #         return True
        #     else:
        #         logger.error(f"Failed to update model {model['orderNo']}.")
        #         return False


    @staticmethod
    def addNewModel(newModel, operations):
        # print('here')
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
            logger.info(f"New model {newModelToAdd.ПоръчкаNo} with id {newModelToAdd.id} added successfully.")

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
            if newModelToAdd and newModelToAdd.productionModelOperations:
                logger.info(f"Operations for new model {newModelToAdd.ПоръчкаNo} added successfully.")
                return newModelToAdd.ПоръчкаNo
            else:
                logger.error(f"Failed to add operations for new model {newModelToAdd.ПоръчкаNo}.")
                return None

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
            modelObleklo = f'{model.WearType}: {model.vidOblekla.OblekloName}' if model.vidOblekla else None
            modelPieces = model.Броя if model else 0
            modelActual = model.Actual if model else False
            return [modelFine, modelMachine, modelYarn, modelObleklo, modelPieces, modelActual]

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
