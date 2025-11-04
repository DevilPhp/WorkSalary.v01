from sqlalchemy import func

from app.database import getDatabase, setDatabase
from app.database.operations import Operation, ProductionModelOperations, OperationsGroup, OperationsGroupForModel
from app.database.workers import OperationType
from app.logger import logger


class OperationsServices:

    @staticmethod
    def deleteOperation(operationId):
        with setDatabase() as session:
            operation = session.query(Operation).filter_by(ОперацияNo=operationId).first()
            if (operation
                    and not operation.operationsGroup
                    and not operation.defaultOperForVidOblekla
                    and not operation.productionModelOperations):
                session.delete(operation)
                session.commit()
                logger.info(f'Operation {operation.ОперацияNo} - {operation.Операция} deleted')
                return True
            else:
                logger.error(f'Operation with id {operationId} not found or has relations')
                return False

    @staticmethod
    def addNewDefaultOperations(operationsName, operType):
        with setDatabase() as session:
            maxId = session.query(func.max(Operation.ОперацияNo)).scalar() or 0
            newOperation = Operation(
                ОперацияNo=maxId + 1,
                Операция=operationsName
            )
            session.add(newOperation)
            session.flush()

            if operType:
                operTypeObj = session.query(OperationType).filter_by(OperTypeID=int(operType)).first()
                newOperation.operationTypes.append(operTypeObj)
                # session.commit()
                logger.info(f'New Operation {newOperation.ОперацияNo} - {newOperation.Операция} added with type {operType}')
                # return [newOperation.ОперацияNo, newOperation.Операция]

            session.commit()
            logger.info(f'New Operation {newOperation.ОперацияNo} - {newOperation.Операция} added')
            return [newOperation.ОперацияNo, newOperation.Операция]

    @staticmethod
    def checkIfOperExistInModel(operId):
        with getDatabase() as session:
            return session.query(Operation).filter_by(ОперацияNo=operId).first() is not None

    @staticmethod
    def addOperationsGroupToModel(modelId, modelName, operations, groupId=None, name=None):
        with setDatabase() as session:

            if not operations and groupId:
                group = session.query(OperationsGroupForModel).filter_by(id=groupId).first()
                session.delete(group)
                session.commit()
                logger.info(f'Operation Group {group.Name} for model {modelId} - {modelName} deleted')
                return True

            dbOperations = session.query(ProductionModelOperations).filter(
                ProductionModelOperations.ПоръчкаNo == modelName, ProductionModelOperations.ОперацияNo.in_(operations)
            ).all()
            print(groupId)
            if groupId:
                group = session.query(OperationsGroupForModel).filter_by(id=groupId).first()
                if group:
                    group.operations = []
                    session.flush()
                    print(operations)
                    for operation in dbOperations:
                        group.operations.append(operation)
                    session.commit()
                    logger.info(f'Operation Group {group.Name} for model {modelId} - {modelName} '
                                f'updated with operations {operations}')
            else:
                newModelGroup = OperationsGroupForModel(
                    Name=name,
                    ModelId=modelId
                )
                for operation in dbOperations:
                    newModelGroup.operations.append(operation)
                    print(operation.Операция)
                session.add(newModelGroup)
                session.commit()
                logger.info(f'Operation Group {newModelGroup.Name} for model {modelId} - {modelName} '
                            f'added with operations {operations}')
            return True

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
    def getGroupOperationsForModel(modelId):
        modelOperationsGroups = {}
        operations = []
        with getDatabase() as session:
            groups = session.query(OperationsGroupForModel).filter_by(ModelId=modelId)\
                .order_by(OperationsGroupForModel.id).all()
            for group in groups:
                if group.operations:
                    operations = [operation.ОперацияNo for operation in group.operations]
                modelOperationsGroups[group.Name] = {
                    'id': group.id,
                    'operations': operations
                }
            return modelOperationsGroups

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
