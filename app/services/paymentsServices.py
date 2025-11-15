from app.logger import logger
from app.utils.appUtils import handle_api_connection
import requests
from config import API_SERVER


class PaymentServices:

    @staticmethod
    @handle_api_connection
    def updatePayPerMin(itemId, currentId, user, dayMins):
        response = requests.post(f"{API_SERVER}/payment/update_pay_per_min",
                                 json={'itemId': itemId, 'currentId': currentId,
                                       'user': user, 'dayMins': dayMins}).json()
        if response['result']:
            if dayMins:
                message = 'Payment '
            else:
                message = 'Night payment '
            logger.info(f"{message}per minute from id {currentId} to id {itemId} - updated by {user}")
            return True

    @staticmethod
    @handle_api_connection
    def getPayPerMin(dayMin=True):
        response = requests.get(f"{API_SERVER}/payment/get_pay_per_min", json={'dayMin': dayMin}).json()
        if response['status'] == 'success':
            return response['data']
        else:
            logger.error("Failed to get payment per minute")
            return []

    @staticmethod
    @handle_api_connection
    def addPayPerMin(user, newEntry, day):
        response = requests.post(f"{API_SERVER}/payment/add_pay_per_min",
                                 json={'user': user, 'day': day, 'newEntry': newEntry}).json()
        if response['status'] == 'success':
            if day:
                message = 'Payment '
            else:
                message = 'Night payment '
            logger.info(f"{message}per minute added - by {user}")
            return True
        else:
            logger.error("Failed to add payment per minute")
            return False

    @staticmethod
    @handle_api_connection
    def deletePayPerMin(user, selectedId, day=True):
        response = requests.post(f"{API_SERVER}/payment/delete_pay_per_min",
                                 json={'user': user, 'id': selectedId, 'day': day}).json()
        if response['status'] =='success':
            if day:
                message = 'payment '
            else:
                message = 'night payment '
            logger.info(f'Deleted {message}per minute: {selectedId} - by {user}')
            return True
        else:
            logger.error("Failed to delete payment per minute")
            return False

    @staticmethod
    @handle_api_connection
    def getHolidaysForYear(selectedYear):
        response = requests.get(f"{API_SERVER}/payment/get_holidays_for_year",
                                json={'selectedYear': selectedYear}).json()
        if response['status'] =='success':
            return response['data']
        else:
            logger.error("Failed to get holidays for year")
            return []

    @staticmethod
    @handle_api_connection
    def addHoliday(name, date, user, selectedYear):
        print(date)
        response = requests.post(f"{API_SERVER}/payment/add_holiday",
                                 json={'name': name, 'date': date, 'user': user, 'selectedYear': selectedYear}).json()
        if response['status'] =='success':
            logger.info(f'Added new holiday: {name} on {date} by {user}')
            return True
        else:
            logger.error("Failed to add holiday")
            return False

    @staticmethod
    @handle_api_connection
    def deleteHoliday(holidayId, year, user):
        response = requests.post(f"{API_SERVER}/payment/delete_holiday",
                                 json={'holidayId': holidayId, 'year': year, 'user': user}).json()
        if response['status'] =='success':
            logger.info(f'Deleted holiday: {holidayId} by {user}')
            return True
        else:
            logger.error("Failed to delete holiday")
            return False

    @staticmethod
    @handle_api_connection
    def getHolidaysYears():
        response = requests.get(f"{API_SERVER}/payment/get_holidays_years").json()
        if response['status'] =='success':
            return response['data']
        else:
            logger.error("Failed to get holidays years")
            return []

    @staticmethod
    @handle_api_connection
    def addHolidaysYear(year, user):
        response = requests.post(f"{API_SERVER}/payment/add_holidays_year",
                                 json={'year': year, 'user': user}).json()
        if response['status'] =='success':
            logger.info(f'Added new holidays year: {year} by {user}')
            return True
        else:
            logger.error("Failed to add holidays year")
            return False
