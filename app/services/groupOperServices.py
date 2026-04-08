import requests

from app.logger import logger
from app.utils.appUtils import handle_api_connection
from config import API_SERVER


class GroupOperationsService:

    #-------GETTERS-------#
    @staticmethod
    @handle_api_connection
    def getInitialData():
        response = requests.get(f'{API_SERVER}/group_operations/get_initial_data').json()
        if response['status'] == 'success':
            logger.info('Successfully fetched initial data for oper groups')
            return response['data']
        else:
            logger.error('Failed to fetch initial data for oper groups')
            return {}

    @staticmethod
    @handle_api_connection
    def getGroups():
        response = requests.get(f'{API_SERVER}/group_operations/get_groups').json()
        if response['status'] =='success':
            logger.info('Successfully fetched groups')
            return response['data']
        else:
            logger.error('Failed to fetch groups')
            return {}


    #-------SETTERS-------#

    @staticmethod
    @handle_api_connection
    def saveOperationsToDB(row):
        response = requests.post(f'{API_SERVER}/group_operations/save_opers', json={'row': row}).json()
        if response['status'] == 'success':
            logger.info('Successfully saved operations to database')
            return response['data']
        else:
            logger.error('Failed to save operations to database')
            return []

    @staticmethod
    @handle_api_connection
    def addOperation(oper):
        response = requests.post(f'{API_SERVER}/group_operations/add_operation', json={'oper': oper}).json()
        if response['status'] =='success':
            logger.info('Successfully added operation')
            return response['data']
        else:
            logger.error('Failed to add operation')
            return False

    @staticmethod
    @handle_api_connection
    def updateOperation(oper):
        response = requests.post(f'{API_SERVER}/group_operations/update_operation', json={'oper': oper}).json()
        if response['status'] =='success':
            logger.info('Successfully updated operation')
            return response['data']
        else:
            logger.error('Failed to update operation')
            return False

    @staticmethod
    def addBranch(nodeType, branchName):
        response = requests.post(f'{API_SERVER}/group_operations/add_branch',
                                 json={'nodeType': nodeType, 'branchName': branchName}).json()
        if response['status'] =='success':
            logger.info('Successfully added branch')
            return response['data']
        else:
            logger.error('Failed to add branch')
            return False

    @staticmethod
    @handle_api_connection
    def editBranch(nodeType, branchId, newBranchName):
        response = requests.post(f'{API_SERVER}/group_operations/edit_branch',
                                 json={'nodeType': nodeType,
                                       'branchId': branchId,
                                       'newBranchName': newBranchName}
                                 ).json()
        if response['status'] =='success':
            logger.info(f'Successfully edited branch id-{branchId}')
            return response['data']
        else:
            logger.error(f'Failed to edit branch id-{branchId}')
            return False
