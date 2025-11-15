import requests
from app.logger import logger
from app.utils.appUtils import handle_api_connection
from config import API_SERVER


class OperationsServices:

    @staticmethod
    @handle_api_connection
    def deleteOperation(operationId):
        response = requests.post(f'{API_SERVER}/operation/delete_operation',
                                 json={'operationId': operationId}).json()
        if response['status'] =='success':
            if response['result'] == 1:
                logger.info(f'Operation {response["ОперацияNo"]} - {response["Операция"]} deleted')
                return True
            elif response['result'] == -1:
                logger.error(f'Error deleting operation {operationId}: has relations')
                return False
        else:
            logger.error(f'Error deleting operation {operationId}: {response["message"]}')
            return False

    @staticmethod
    @handle_api_connection
    def addNewDefaultOperations(operationsName, operType):
        response = requests.post(f'{API_SERVER}/operation/add_operation',
                                 json={'operationsName': operationsName, 'operType': operType}).json()
        if response['status'] =='success':
            if response["ОперацияNo"] and response["Операция"]:
                logger.info(f'New Operation {response["ОперацияNo"]} - {response["Операция"]} added')
                return [response["ОперацияNo"], response["Операция"]]
            else:
                logger.error(f'Error adding new Operation: {operationsName}')
                return []
        else:
            logger.error(f'Error adding new Operation: {operationsName}')
            return []

    @staticmethod
    @handle_api_connection
    def addOperationsGroupToModel(modelId, modelName, operations, groupId=None, name=None):
        response = requests.post(f'{API_SERVER}/operation/add_group_to_model',
                                 json={'modelId': modelId, 'modelName': modelName, 'operations': operations,
                                       'groupId': groupId, 'name': name}).json()
        if response['status'] =='success':
            if response['result'] == -1:
                logger.info(f'Operation Group {response["groupName"]} for model {modelId} - {modelName} deleted')
                return True
            elif response['result'] == 1:
                logger.info(f'Operation Group {response["groupName"]} for model {modelId} - {modelName} '
                            f'updated with operations {operations}')
                return True
            else:
                logger.info(f'Operation Group {response["groupName"]} for model {modelId} - {modelName} '
                            f'added with operations {operations}')
                return True
        else:
            logger.error(f'Error adding Operation Group to model {modelId}')
            return False


    @staticmethod
    @handle_api_connection
    def addOperationToGroup(operations, groupId=None, name=None):
        response = requests.post(f'{API_SERVER}/operation/add_operation_to_group',
                                 json={'operations': operations, 'groupId': groupId, 'name': name}).json()
        if response['status'] =='success':
            if response['result'] == -1:
                logger.info(f'Operation Group {response["groupName"]} deleted')
                return True
            elif response['result'] == 1:
                logger.info(f'Operation Group {response["groupName"]} updated with operations {operations}')
                return True
            else:
                logger.info(f'Operation Group {response["groupName"]} added with operations {operations}')
                return True
        else:
            logger.error(f'Error adding Operation Group: {operations}')
            return False

    @staticmethod
    @handle_api_connection
    def getOperationsGroups():
        response = requests.get(f'{API_SERVER}/operation/get_groups').json()
        if response['status'] =='success':
            return response['result']
        else:
            logger.error('Error getting Operation Groups')
            return []

    @staticmethod
    @handle_api_connection
    def getGroupOperationsForModel(modelId):
        response = requests.get(f'{API_SERVER}/operation/get_group_operations_for_model/{modelId}').json()
        if response['status'] =='success':
            return response['result']
        else:
            logger.error('Error getting Group Operations for Model')
            return []

    @staticmethod
    @handle_api_connection
    def getAllOperations():
        response = requests.get(f'{API_SERVER}/operation/get_all_operations').json()
        if response['status'] =='success':
            returnedData = {int(key): value for key, value in response['result'].items()}
            return returnedData
        else:
            logger.error('Error getting All Operations')
            return []

    @staticmethod
    @handle_api_connection
    def updateOperationName(operId, operName):
        response = requests.post(f'{API_SERVER}/operation/update_operation_name',
                                 json={'operId': operId, 'operName': operName}).json()
        if response['status'] =='success':
            if response['result']:
                logger.info(f'Operation with ID {operId} updated to {operName}')
                return True
            else:
                logger.error(f'Operation with ID {operId} not found')
                return False
        else:
            logger.error(f'Error updating Operation Name: {operId} - {operName}')
            return False

    @staticmethod
    @handle_api_connection
    def getOperationsForModel(orderId):
        response = requests.get(f'{API_SERVER}/operation/get_operations_for_model/{orderId}').json()
        if response['status'] =='success':
            return response['result']
        else:
            logger.error('Error getting Operations for Model')
            return []
