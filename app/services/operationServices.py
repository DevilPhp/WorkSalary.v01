from app.database import getDatabase, setDatabase
from app.database.operations import Operation, ProductionModelOperations, OperationsGroup

class OperationsServices:

    @staticmethod
    def getOperationsGroups():
        operationsGroups = {}
        operations = []
        with getDatabase() as session:
            groups = session.query(OperationsGroup).order_by(OperationsGroup.id).all()
            for group in groups:
                if group.operations:
                    operations = [operation.ОперацияNo for operation in group.operations]
                operationsGroups[group.id] = {
                    'name': group.Name,
                    'operations': operations
                }
            return operationsGroups


    @staticmethod
    def getAllOperations():
        with getDatabase() as session:
            return session.query(Operation).order_by(Operation.ОперацияNo.asc()).all()

    @staticmethod
    def getOperationsForModel(orderId):
        with getDatabase() as session:
            print(orderId)
            return session.query(ProductionModelOperations).filter_by(OrderId=orderId).all()
