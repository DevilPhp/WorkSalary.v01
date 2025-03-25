from app.database import getDatabase, setDatabase
from app.database.operations import DefaultOperForVidObleklo, Operation

class OperationsServices:
    @staticmethod
    def getAllOperations():
        with getDatabase() as session:
            return session.query(Operation).order_by(Operation.ОперацияNo.asc()).all()
