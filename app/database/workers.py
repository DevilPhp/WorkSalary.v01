from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base, SessionLocal

class Worker(Base):
    __tablename__ = "workers"
    id = Column(Integer, primary_key=True, index=True)


class Cehove(Base):
    __tablename__ = "cehove"
    id = Column(Integer, primary_key=True)
    Група = Column(String, nullable=True)
    ГрупаName = Column(String, nullable=True)
    Вид = Column(String, nullable=True)
    SupervisorNo = Column(Integer, nullable=True)


class WorkerPosition(Base):
    __tablename__ = "workerPositions"
    # id = Column(Integer, primary_key=True)
    ДлъжностКод = Column(Integer, primary_key=True)
    Длъжност = Column(String, nullable=True)
    Коефициент = Column(Float, nullable=True)
    ВидОперация = Column(Integer, ForeignKey("operationTypes.OperTypeID"), nullable=True)

    operationType = relationship("OperationType", back_populates="workerPositions")


class OperationType(Base):
    __tablename__ = "operationTypes"
    OperTypeID = Column(Integer, primary_key=True)
    OperName = Column(String, nullable=True)

    workerPositions = relationship("WorkerPosition", back_populates="operationType")

