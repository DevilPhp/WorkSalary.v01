import requests

from app.logger import logger
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
    def getNewModelsAndClients():
        response = requests.get(f'{API_SERVER}/model/get_new_models_and_clients').json()
        if response['status'] =='success':
            return response['data']
        else:
            logger.error('Failed to get new models and clients')
            return []


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

    @staticmethod
    @handle_api_connection
    def getForModelsGroups():
        response = requests.get(f'{API_SERVER}/model/get_for_models_groups').json()
        if response['status'] == 'success':
            return response['modelsDict']
        else:
            logger.error('Failed to get models groups')
            return None

    @staticmethod
    # @handle_api_connection
    def checkIfOperationsCanBeDeleted(model, removedOperations):
        response = requests.get(f'{API_SERVER}/model/check_if_operations_can_be_deleted',
                                 json={'modelId': model['orderNo'], 'operations': removedOperations}).json()
        if response['status'] =='success':
            return response['cantBeDeleted']
        else:
            logger.error(f'Failed to check if operations can be deleted for {model["orderNo"]}')
            return None

    @staticmethod
    @handle_api_connection
    def effectChangedOperTimes(changedOperations, month, modelId):
        response = requests.post(f'{API_SERVER}/model/effect_changed_oper_times',
                                 json={'changedOperations': changedOperations,
                                       'month': month, 'modelId': modelId}).json()
        if response['status'] =='success':
            logger.info(f'Changed operation times for month {month} updated successfully')
            return True
        else:
            logger.error(f'No time papers found for month {month}')
            return False

    @staticmethod
    @handle_api_connection
    def setModelProductionStatus(modelId, status):
        response = requests.post(f'{API_SERVER}/model/set_model_production_status',
                                 json={'modelId': modelId, 'status': status}).json()
        if response['status'] =='success':
            logger.info(f'Production status for model {modelId} updated successfully')
            return True
        else:
            logger.error(f'Failed to update production status for model {modelId}')
            return False

    @staticmethod
    @handle_api_connection
    def updateActualStatus(modelId, status):
        response = requests.post(f'{API_SERVER}/model/update_model_actual',
                                 json={'modelId': modelId, 'status': status}).json()
        if response['status'] =='success':
            logger.info(f'Actual status for model {modelId} updated successfully')
            return True
        else:
            logger.error(f'Failed to update actual status for model {modelId}')
            return False

    @staticmethod
    @handle_api_connection
    def updateModel(model, modelFromTimePaper,  operations, removedOperations, user):
        response = requests.post(f'{API_SERVER}/model/update_model',
                                 json={'modelId': model, 'modelFromTimePaper': modelFromTimePaper,
                                       'operations': operations, 'removedOperations': removedOperations,
                                       'user': user}).json()
        if response['status'] =='success':
            if model:
                logger.info(f'Model {model["orderNo"]} updated successfully')
                return True
            else:
                logger.info(f'New model added successfully')
                logger.info(f'Model {modelFromTimePaper} updated successfully')
                return True
        else:
            logger.error(f'Failed to update model {model["orderNo"]}')
            return False

    @staticmethod
    @handle_api_connection
    def addNewModel(newModel, operations):
        response = requests.post(f'{API_SERVER}/model/add_new_model',
                                 json={'model': newModel, 'operations': operations}).json()
        if response['status'] =='success':
            logger.info(f'New model {newModel["orderNo"]} added successfully')
            return [newModel["orderNo"], response['modelId']]
        else:
            logger.error(f'Failed to add new model {newModel["orderNo"]}')
            return None

    @staticmethod
    @handle_api_connection
    def deleteModel(modelId):
        response = requests.post(f'{API_SERVER}/model/delete_model', json={'modelId': modelId}).json()
        if response['status'] =='success':
            logger.info(f'Model {modelId} deleted successfully')
            return 1
        elif response['status'] == 'operationsExist':
            logger.error(f'Operations for model {modelId} exists in Time papers')
            return 2
        else:
            logger.error(f'Failed to delete model {modelId}')
            return 0

    @staticmethod
    @handle_api_connection
    def getModelsForClient(clientId):
        response = requests.get(f'{API_SERVER}/model/get_models_for_client/{clientId}').json()
        if response['status'] =='success':
            logger.info(f'Models for client {clientId} fetched successfully')
            return response['models']
        else:
            logger.error(f'Failed to get models for client {clientId}')
            return []

    @staticmethod
    @handle_api_connection
    def getModelsYearsForClient(clientId):
        response = requests.get(f'{API_SERVER}/model/get_model_years_for_client/{clientId}').json()
        if response['status'] =='success':
            logger.info(f'Models years for client {clientId} fetched successfully')
            return response['years']
        else:
            logger.error(f'Failed to get models years for client {clientId}')
            return []

    @staticmethod
    @handle_api_connection
    def getProductionForClient(clientId, year):
        response = requests.get(f'{API_SERVER}/model/get_production_for_client/{clientId}/{year}').json()
        if response['status'] =='success':
            logger.info(f'Production for client {clientId} and year {year} fetched successfully')
            return response['models']
        else:
            logger.error(f'Failed to get production for client {clientId} and year {year}')
            return []

    @staticmethod
    @handle_api_connection
    def getModelInfo(modelId):
        response = requests.get(f'{API_SERVER}/model/get_model_info/{modelId}').json()
        if response['status'] =='success':
            logger.info(f'Model info for {modelId} fetched successfully')
            return response['modelInfo']
        else:
            logger.error(f'Failed to get model info for {modelId}')
            return []

    @staticmethod
    def getAllModelTypes():
        response = requests.get(f'{API_SERVER}/model/get_all_model_types').json()
        if response['status'] =='success':
            logger.info(f'All model types fetched successfully')
            return response['modelTypes']
        else:
            logger.error(f'Failed to get all model types')
            return {}

    @staticmethod
    def getVidObjekla():
        responde = requests.get(f'{API_SERVER}/model/get_vid_objekla').json()
        if responde['status'] =='success':
            logger.info(f'All vidObjekla fetched successfully')
            return responde['vidObjekla']
        else:
            logger.error(f'Failed to get all vidObjekla')
            return {}

    @staticmethod
    def getMachines():
        response = requests.get(f'{API_SERVER}/model/get_machines').json()
        if response['status'] =='success':
            logger.info(f'All machines fetched successfully')
            return response['machines']
        else:
            logger.error(f'Failed to get all machines')
            return {}

    @staticmethod
    def getYarns():
        response = requests.get(f'{API_SERVER}/model/get_yarns').json()
        if response['status'] =='success':
            logger.info(f'All yarns fetched successfully')
            return response['yarns']
        else:
            logger.error(f'Failed to get all yarns')
            return {}

    @staticmethod
    @handle_api_connection
    def getOperationsForModelType(vidObleklo):
        response = requests.get(f'{API_SERVER}/model/get_operations_for_model_type/{vidObleklo}').json()
        if response['status'] =='success':
            logger.info(f'Operations for model type {vidObleklo} fetched successfully')
            return response['operations']
        else:
            logger.error(f'Failed to get operations for model type {vidObleklo}')
            return {}

    @staticmethod
    @handle_api_connection
    def saveOperationsForModelType(modelTypeId, operations):
        response = requests.post(f'{API_SERVER}/model/save_operations_for_model_type',
                                 json={'modelTypeId': modelTypeId, 'operations': operations}).json()
        if response['status'] =='success':
            logger.info(f'Operations for model type {modelTypeId} saved successfully')
            return True
        else:
            logger.error(f'Failed to save operations for model type {modelTypeId}')
            return False

    @staticmethod
    @handle_api_connection
    def getExistingWorkingPlaces(modelId):
        response = requests.get(f'{API_SERVER}/model/get_existing_working_places/{modelId}').json()
        if response['status'] == 'success':
            logger.info('Retrieved existing working places')
            return response['workingPlaces']
        else:
            logger.error('Failed to get existing working places')
            return []

    @staticmethod
    @handle_api_connection
    def addWorkingPlace(modelId, workingPlaces):
        response = requests.post(f'{API_SERVER}/model/add_working_place/{modelId}',
                                 json={'workingPlaces': workingPlaces}).json()
        if response['status'] =='success':
            logger.info(f'Added working place to model {modelId}')
            return True
        else:
            logger.error(f'Failed to add working place to model {modelId}')
            return False
