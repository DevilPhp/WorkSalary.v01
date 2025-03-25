from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey, DateTime, Boolean, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base, SessionLocal
from app.database.models import VidObleklo

modelOperationsType = Table(
    'modelOperationsTypes', Base.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('ModelOpID', Integer, ForeignKey('operations.ОперацияNo'), primary_key=True),
    Column('OpTypeID', Integer, ForeignKey('operationTypes.OperTypeID'), nullable=True)
)


class Operation(Base):
    __tablename__ = 'operations'
    ОперацияNo = Column(Integer, primary_key=True)
    Операция = Column(String, nullable=True)

    operationTypes = relationship('OperationType', secondary='modelOperationsTypes', back_populates='operations')
    defaultOperForVidOblekla = relationship('DefaultOperForVidObleklo', back_populates='operations')


class DefaultOperForVidObleklo(Base):
    __tablename__ = 'defaultOperForVidOblekla'
    id = Column(Integer, primary_key=True, autoincrement=True)
    OblekloVid = Column(Integer, ForeignKey('vidOblekla.OblekloVid'), primary_key=True)
    ОперацияNo = Column(Integer, ForeignKey('operations.ОперацияNo'), primary_key=True)
    defaultTime = Column(Float, default=0)

    operations = relationship('Operation', back_populates='defaultOperForVidOblekla')
    vidOblekla = relationship('VidObleklo', back_populates='defaultOperForVidOblekla')

