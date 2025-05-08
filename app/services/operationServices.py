from app.database import getDatabase, setDatabase
from app.database.operations import Operation, ProductionModelOperations, OperationsGroup
from app.logger import logger


class OperationsServices:

    @staticmethod
    def checkIfOperExistInModel(operId):
        with getDatabase() as session:
            return session.query(Operation).filter_by(ОперацияNo=operId).first() is not None

    @staticmethod
    def addOperationToGroup(operations, groupId=None, name=None):
        with setDatabase() as session:

            if not operations and groupId:
                group = session.query(OperationsGroup).filter_by(id=groupId).first()
                session.delete(group)
                session.commit()
                logger.info(f'Operation Group {group.Name} deleted')
                return True

            dbOperations = session.query(Operation).filter(Operation.ОперацияNo.in_(operations)).all()
            if groupId:
                group = session.query(OperationsGroup).filter_by(id=groupId).first()
                if group:
                    group.operations = []
                    session.flush()
                    for operation in dbOperations:
                        group.operations.append(operation)
                session.commit()
                logger.info(f'Operation Group {group.Name} updated with operations {operations}')
            else:
                new_group = OperationsGroup(Name=name)
                for operation in dbOperations:
                    new_group.operations.append(operation)
                session.add(new_group)
                session.commit()
                logger.info(f'New Operation Group {name} created with operations {operations}')
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
        returnedData = {}
        with getDatabase() as session:
            operations = session.query(Operation).order_by(Operation.ОперацияNo.asc()).all()
            for operation in operations:
                returnedData[operation.ОперацияNo] = {
                    'name': operation.Операция,
                    'operationType': operation.operationTypes[0].OperName if operation.operationTypes else None,
                }
            return returnedData

    @staticmethod
    def updateOperationName(operId, operName):
        with setDatabase() as session:
            operation = session.query(Operation).filter_by(ОперацияNo=operId).first()
            if operation:
                operation.Операция = operName
                session.commit()
                logger.info(f'Operation with ID {operId} updated to {operName}')
                return True
            else:
                logger.error(f'Operation with ID {operId} not found')
                return False

    @staticmethod
    def getOperationsForModel(orderId):
        with getDatabase() as session:
            return session.query(ProductionModelOperations).filter_by(OrderId=orderId).all()
