from app.database import getDatabase, setDatabase
from app.database.operations import Operation, ProductionModelOperations, OperationsGroup

class OperationsServices:

    @staticmethod
    def addOperationToGroup(operations, groupId=None, name=None):
        with setDatabase() as session:
            dbOperations = session.query(Operation).filter(Operation.ОперацияNo.in_(operations)).all()
            if groupId:
                group = session.query(OperationsGroup).filter_by(id=groupId).first()
                if group:
                    group.operations = []
                    session.flush()
                    for operation in dbOperations:
                        group.operations.append(operation)
                session.commit()
            else:
                new_group = OperationsGroup(Name=name)
                for operation in dbOperations:
                    new_group.operations.append(operation)
                session.add(new_group)
                session.commit()
            return True

    @staticmethod
    def getOperationsGroups():
        operationsGroups = {}
        operations = []
        with getDatabase() as session:
            groups = session.query(OperationsGroup).order_by(OperationsGroup.id).all()
            for group in groups:
                if group.operations:
                    operations = [operation.ОперацияNo for operation in group.operations]
                operationsGroups[group.Name] = {
                    'id': group.id,
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
