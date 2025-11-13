from app.logger import logger
import requests
from app.utils.appUtils import handle_api_connection
from config import API_SERVER


class UserServices:

    @staticmethod
    @handle_api_connection
    def registerNewUser(data):
        responde = requests.post(f'{API_SERVER}/user/register', json=data).json()
        if responde['status'] == 'success':
            result = int(responde['result'])
            if result == 1:
                logger.info(f"User: {data['Потребител']} has been registered successfully")
            elif result == -1:
                logger.error(f"Username {data['Потребител']} already exists")
            return result
        else:
            logger.error(f"Failed to register user: {data['Потребител']}")
            return 0

    @staticmethod
    @handle_api_connection
    def editUser(userId, data):
        responde = requests.post(f'{API_SERVER}/user/edit', json={'id': userId, 'data': data}).json()
        if responde['status'] =='success':
            logger.info(f"User with ID {userId} - {responde['username']} has been edited successfully")
            return responde['username']
        else:
            logger.error(f"Failed to edit user with ID {userId}")
            return None

    @staticmethod
    @handle_api_connection
    def deleteUser(rowId):
        responde = requests.post(f'{API_SERVER}/user/delete', json={'id': rowId}).json()
        if responde['status'] =='success':
            logger.info(f"User with ID {responde['id']} - {responde['username']} has been deleted successfully")
            return True
        else:
            logger.error(f"User with ID {responde['id']} - {responde['username']} does not exist")
            return False

    @staticmethod
    def loginUser(username, password):
        responde = requests.post(f'{API_SERVER}/user/login',
                                 json={'username': username, 'password': password}).json()
        if responde['status'] == 'success':
            logger.info(f"User {username} has logged in successfully")
            return True
        else:
            logger.error(f"Invalid username or password for user {username}")
            return False
