from app.database import getDatabase, setDatabase
from app.database.operations import DefaultOperForVidObleklo, Operation, ProductionModelOperations

class OperationsServices:
    @staticmethod
    def getAllOperations():
        with getDatabase() as session:
            return session.query(Operation).order_by(Operation.ОперацияNo.asc()).all()

    @staticmethod
    def getOperationsForModel(orderId):
        with getDatabase() as session:
            print(orderId)
            return session.query(ProductionModelOperations).filter_by(OrderId=orderId).all()
