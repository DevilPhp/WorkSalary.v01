from app.logger import logger
import requests
from config import API_SERVER
from app.utils.appUtils import handle_api_connection


class WorkerServices:
    @staticmethod
    @handle_api_connection
    def addNewOperationType(data, rows):
        if data:
            response = requests.post(f'{API_SERVER}/worker/new_operation_type',
                                     json={'rows': rows, 'data': data}).json()
            if response['status'] == 'success':
                logger.info(f'OperationType {response["data"][0]} - {response["data"][1]} added')
                return True
            else:
                logger.error('Failed to add new OperationType')
                return False
        else:
            logger.error('No data provided for new OperationType')
            return False

    @staticmethod
    @handle_api_connection
    def deleteSelectedOperationType(rowId):
        response = requests.post(f'{API_SERVER}/worker/delete_operation_type', json={'rowId': rowId}).json()
        if response['status'] == 'success':
            if response['data'] == 1:
                logger.info(f'OperationType {rowId} deleted')
                return 1
            elif response['data'] == -1:
                logger.error(f'OperationType {rowId} has associated TimePapers, cannot delete')
                return -1
        else:
            logger.error('Failed to delete OperationType')
            return 0

    @staticmethod
    @handle_api_connection
    def addNewWorkerPosition(data, rows):
        if data:
            response = requests.post(f'{API_SERVER}/worker/new_worker_position',
                                     json={'rows': rows, 'data': data}).json()
            if response['status'] == 'success':
                logger.info(f'WorkerPosition {response["data"][0]} - {response["data"][1]} added')
                return True
            else:
                logger.error('Failed to add new WorkerPosition')
                return False
        else:
            logger.error('No data provided for new WorkerPosition')
            return False

    @staticmethod
    @handle_api_connection
    def deleteSelectedWorkerPosition(rowId):
        response = requests.post(f'{API_SERVER}/worker/delete_worker_position', json={'rowId': rowId}).json()
        if response['data'] == 1:
            logger.info(f'WorkerPosition {rowId} deleted')
            return 1
        elif response['data'] == -1:
            logger.error(f'WorkerPosition {rowId} has workers/opersType associated, cannot delete')
            return -1
        else:
            logger.error(f'WorkerPosition {rowId} not found')
            return 0

    @staticmethod
    @handle_api_connection
    def addNewCehove(data):
        if data:
            response = requests.post(f'{API_SERVER}/worker/new_cheh',
                                     json={'data': data}).json()
            if response['status'] == 'success':
                logger.info(f'Cehove {response["data"][0]} - {response["data"][1]} added')
                return True
            else:
                logger.error('Failed to add new Cehove')
                return False
        else:
            logger.error('No data provided for new Cehove')
            return False

    @staticmethod
    @handle_api_connection
    def deleteSelectedCehove(rowId):
        response = requests.post(f'{API_SERVER}/worker/delete_ceh', json={'rowId': rowId}).json()
        if response['status'] == 'success':
            if response['result'] == 1:
                logger.info(f"Ceh {rowId} deleted")
                return 1
            elif response['result'] == -1:
                logger.error(f'Ceh {rowId} has workers associated, cannot delete')
                return -1
            else:
                logger.error(f'Ceh {rowId} not found')
                return 0
        else:
            logger.error('Failed to delete Ceh')
            return 0

    @staticmethod
    @handle_api_connection
    def getWorkersForCehove():
        response = requests.get(f'{API_SERVER}/worker/workers_for_ceh').json()
        if response['status'] =='success':
            return response['data']
        else:
            logger.error('Failed to get workers for Ceh')
            return []

    @staticmethod
    @handle_api_connection
    def getOperationTypes():
        response = requests.get(f'{API_SERVER}/worker/operations_types').json()
        if response['status'] == 'success':
            return response['data']
        else:
            logger.error('Failed to get OperationType')
            return []

    @staticmethod
    @handle_api_connection
    def deleteWorker(workerId):
        response = requests.post(f'{API_SERVER}/worker/delete_worker', json={'workerId': workerId}).json()
        if response['status'] =='success':
            if response['result'] == 1:
                logger.info(f'Worker {workerId} deleted')
                return True
            elif response['result'] == -1:
                logger.error(f'Worker {workerId} has time papers associated, cannot delete')
                return False
            else:
                logger.error(f'Worker {workerId} not found')
                return False
        else:
            logger.error('Failed to delete worker')
            return False

    @staticmethod
    @handle_api_connection
    def setWorker(workerData):
        response = requests.post(f'{API_SERVER}/worker/set_worker', json={'data': workerData}).json()
        if response['status'] =='success':
            if response['result'] == 1:
                logger.info(f'Worker {workerData["id"]} set')
                return True
            elif response['result'] == 0:
                logger.error(f'Worker with ID {workerData["id"]} not found')
                return False
        else:
            logger.error('Failed to set worker')
            return False

    @staticmethod
    @handle_api_connection
    def getCehove():
        response = requests.get(f'{API_SERVER}/worker/cehove').json()
        if response['status'] == 'success':
            return response['data']
        else:
            logger.error('Failed to get Cehove')
            return []

    @staticmethod
    @handle_api_connection
    def getPositions():
        response = requests.get(f'{API_SERVER}/worker/positions').json()
        if response['status'] == 'success':
            return response['data']
        else:
            logger.error('Failed to get positions')
            return []

    @staticmethod
    @handle_api_connection
    def getPaymentTypes():
        response = requests.get(f'{API_SERVER}/worker/payment_types').json()
        if response['status'] == 'success':
            return response['data']
        else:
            logger.error('Failed to get payment types')
            return []

    @staticmethod
    @handle_api_connection
    def getWorkerInfo(workerId):
        response = requests.get(f'{API_SERVER}/worker/worker_info', json={'workerId': workerId}).json()
        if response['status'] == 'success':
            return response['data']
        else:
            logger.error('Failed to get worker info')
            return {}

    @staticmethod
    @handle_api_connection
    def getWorkersInfo():
        response = requests.get(f'{API_SERVER}/worker/workers_info').json()
        if response['status'] == 'success':
            return response['data']
        else:
            logger.error('Failed to get workers info')
            return []

    @staticmethod
    @handle_api_connection
    def getWorkerDataForPayments(workerId):
        response = requests.get(f'{API_SERVER}/worker/worker_data_for_payments', json={'workerId': workerId}).json()
        if response['status'] == 'success':
            return response['data']
        else:
            logger.error('Failed to get worker data for payments')
            return {}

    @staticmethod
    @handle_api_connection
    def getPaymentsDetailsForWorker(workerId, startDate, endDate):
        response = requests.get(f'{API_SERVER}/worker/payments_details_for_worker',
                                 json={'workerId': workerId, 'startDate': startDate, 'endDate': endDate}).json()
        if response['status'] =='success':
            return response['data']
        else:
            logger.error('Failed to get payments details for worker')
            return []

    @staticmethod
    @handle_api_connection
    def getInfoForPayments(startDate, endDate):
        strStartDate = startDate.strftime('%Y-%m-%d')
        strEndDate = endDate.strftime('%Y-%m-%d')
        responde = requests.post(f'{API_SERVER}/worker/payments',
                                 json={'start': strStartDate, 'end': strEndDate}).json()
        if responde['status'] == 'success':
            return responde['data']
        else:
            return False

    @staticmethod
    @handle_api_connection
    def updateWorkingShift(shiftId, data):
        response = requests.post(f'{API_SERVER}/worker/update_working_shift',
                                 json={'shiftId': shiftId, 'data': data}).json()
        if response['status'] =='success':
            logger.info(f"Working shift updated: {shiftId}")
            return True
        else:
            logger.error('Failed to update working shift')
            return False

    @staticmethod
    @handle_api_connection
    def addWorkingShift(newShiftData):
        response = requests.post(f'{API_SERVER}/worker/add_working_shift', json={'data': newShiftData}).json()
        if response['status'] =='success':
            logger.info(f"New working shift added: {response['newShiftId']}")
            return True
        else:
            logger.error('Failed to add working shift')
            return False

    @staticmethod
    @handle_api_connection
    def deleteWorkingShift(shiftId):
        response = requests.post(f'{API_SERVER}/worker/delete_working_shift', json={'shiftId': shiftId}).json()
        if response['status'] =='success':
            if response['result'] == 1:
                logger.info(f"Working shift deleted: {shiftId}")
                return True
            elif response['result'] == 0:
                logger.error(f"Working shift with time papers associated: {shiftId}")
                return False
        else:
            logger.error('Failed to delete working shift')
            return False

    @staticmethod
    @handle_api_connection
    def deleteTimePapers(slectedIds):
        response = requests.post(f'{API_SERVER}/worker/delete_time_papers', json={'timePaperIds': slectedIds}).json()
        if response['status'] =='success':
            logger.info(f"Time papers deleted: {slectedIds}")
            return True
        else:
            logger.error('Failed to delete time papers')
            return False

    @staticmethod
    @handle_api_connection
    def updateTimePaperPieces(operId, newPieces, newTime, nightShiftMins):
        response = requests.post(f'{API_SERVER}/worker/update_time_paper_pieces',
                                 json={'operId': operId, 'newPieces': newPieces,
                                       'newTime': newTime, 'nightShiftMins': nightShiftMins}).json()
        if response['status'] =='success':
            logger.info(f"Time paper operation updated: {operId} New pieces: {newPieces}, New time: {newTime}")
            return True
        else:
            logger.error(f"Unable to update time paper operation: {operId}")
            return False

    @staticmethod
    @handle_api_connection
    def addNewTimePaperAndOperation(timePaperData):
        response = requests.post(f'{API_SERVER}/worker/add_time_paper_and_operation',
                                 json={'timePaperData': timePaperData}).json()
        if response['status'] == 'success':
            logger.info(f"New time paper and operation added: {timePaperData}")
            return response['newTimePaperId']
        else:
            logger.error(f"Unable to add new time paper and operation: {timePaperData}")
            return None

    @staticmethod
    @handle_api_connection
    def updateTimePaperAndOperation(timePaperData):
        response = requests.post(f'{API_SERVER}/worker/update_time_paper_and_operation',
                                 json={'timePaperData': timePaperData}).json()
        if response['status'] =='success':
            logger.info(f"Time paper updated: {timePaperData}")
            return True
        else:
            logger.error(f"Unable to update time paper: {timePaperData}")
            return False

    @staticmethod
    @handle_api_connection
    def getWorkers():
        response = requests.get(f'{API_SERVER}/worker/get_workers').json()
        if response['status'] =='success':
            return response['data']
        else:
            logger.error('Failed to get workers')
            return []

    @staticmethod
    @handle_api_connection
    def getExistingTimePaperShift(timePaperId):
        response = requests.get(f'{API_SERVER}/worker/get_existing_time_paper_shift',
                                json={'timePaperId': timePaperId}).json()
        if response['status'] =='success':
            return response['returnedShiftInfo']
        else:
            logger.error('Failed to get existing time paper shift')
            return None

    @staticmethod
    @handle_api_connection
    def getTimePapersForDate(date, workerId, showAll=False):
        response = requests.get(f'{API_SERVER}/worker/get_time_papers_for_date',
                                json={'date': date, 'workerId': workerId, 'showAll': showAll}).json()
        if response['status'] =='success':
            return response['returnedData']
        else:
            logger.error('Failed to get time papers for date')
            return []

    @staticmethod
    @handle_api_connection
    def getWorkingShiftsForEdit():
        response = requests.get(f'{API_SERVER}/worker/get_working_shifts_for_edit').json()
        return response['data']

    @staticmethod
    @handle_api_connection
    def getWorkingShifts():
        response = requests.get(f'{API_SERVER}/worker/get_working_shifts').json()
        return response['data']

