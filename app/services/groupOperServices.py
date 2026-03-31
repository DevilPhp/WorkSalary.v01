import requests

from app.logger import logger
from app.utils.appUtils import handle_api_connection
from config import API_SERVER


class GroupOperationsService:
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
    def saveOperationsToDB(row):
        response = requests.post(f'{API_SERVER}/group_operations/save_opers', json={'row': row}).json()
        if response['status'] == 'success':
            logger.info('Successfully saved operations to database')
            return response['data']
        else:
            logger.error('Failed to save operations to database')
            return []
