from app.database import getDatabase
from app.database.models import VidObleklo


class ModelService:
    @staticmethod
    def getAllModelTypes():
        with getDatabase() as session:
            return session.query(VidObleklo).order_by(VidObleklo.OblekloVid.asc()).all()


    @staticmethod
    def getOperationsForModelType(vidObleklo):
        with getDatabase() as session:
            operations = session.query(VidObleklo).filter_by(VidObleklo=vidObleklo).all()
            if operations:
                return session.query(VidObleklo).filter_by(OblekloVid=vidObleklo).all()
            else:
                return None
