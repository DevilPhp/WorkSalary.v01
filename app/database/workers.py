from sqlalchemy import Column, Integer, String, Float, Enum
from app.database import Base, SessionLocal

class Worker(Base):
    __tablename__ = "workers"
    id = Column(Integer, primary_key=True, index=True)


class Cehove(Base):
    __tablename__ = "cehove"
    id = Column(Integer, primary_key=True)
    group = Column(String, nullable=True)
    groupName = Column(String, nullable=True)
    type = Column(String, nullable=True)
    supervisorNo = Column(Integer, nullable=True)


class WorkerPosition(Base):
    __tablename__ = "workerPositions"
    id = Column(Integer, primary_key=True)
    positionName = Column(String, nullable=True)

