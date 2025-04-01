from app.database import getDatabase, setDatabase
from app.database.models import VidObleklo, Client, ProductionModel, Machine, Yarn
from app.database.operations import DefaultOperForVidObleklo, Operation


class ModelService:

    @staticmethod
    def getDfaultOperations(vidOblekloId):
        with getDatabase() as session:
            return session.query(VidObleklo).filter_by(OblekloVid=vidOblekloId).first().defaultOperForVidOblekla

    @staticmethod
    def getClients():
        with getDatabase() as session:
            return session.query(Client).all()

    @staticmethod
    def getAllModels():
        with getDatabase() as session:
            return session.query(ProductionModel).all()

    @staticmethod
    def getModelsForClient(clientId):
        with getDatabase() as session:
            return session.query(ProductionModel).filter_by(ClientID=clientId).all()

    @staticmethod
    def getAllModelTypes():
        with getDatabase() as session:
            return session.query(VidObleklo).order_by(VidObleklo.OblekloVid.asc()).all()

    @staticmethod
    def getVidObjekla():
        returnedData = {}
        with getDatabase() as session:
            vidObjekla = session.query(VidObleklo).order_by(VidObleklo.OblekloVid.asc()).all()
            for vidObleklo in vidObjekla:
                returnedData[vidObleklo.OblekloName] = vidObleklo.OblekloVid
            return returnedData

    @staticmethod
    def getMachines():
        returnedData = {}
        with getDatabase() as session:
            machines = session.query(Machine).order_by(Machine.MachineId.asc()).all()
            for machine in machines:
                returnedData[machine.MachineType] = [machine.MachineId, machine.MachineFine]
            return returnedData

    @staticmethod
    def getYarns():
        returnedData = {}
        with getDatabase() as session:
            yarns = session.query(Yarn).order_by(Yarn.YarnID.asc()).all()
            for yarn in yarns:
                returnedData[yarn.ПреждаТип] = [yarn.YarnID]
            return returnedData

    @staticmethod
    def getOperationsForModelType(vidObleklo):
        with getDatabase() as session:
            operations = session.query(DefaultOperForVidObleklo).filter_by(OblekloVid=vidObleklo).all()
            if operations:
                return operations

    @staticmethod
    def saveOperationsForModelType(modelTypeId, operations):
        with setDatabase() as session:
            if session.query(DefaultOperForVidObleklo).filter_by(OblekloVid=modelTypeId).all():
                session.query(DefaultOperForVidObleklo).filter_by(OblekloVid=modelTypeId).delete()
            for index, operation in enumerate(operations):
                newOperation = DefaultOperForVidObleklo(OblekloVid=modelTypeId,
                                                        ОперацияNo=operation[0],
                                                        defaultTime=float(operation[2]))
                session.add(newOperation)
            return True
