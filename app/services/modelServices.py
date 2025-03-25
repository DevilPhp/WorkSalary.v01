from app.database import getDatabase
from app.database.models import VidObleklo


class ModelService:
    @staticmethod
    def getAllModelTypes():
        with getDatabase() as session:
            return session.query(VidObleklo).order_by(VidObleklo.OblekloVid.asc()).all()
