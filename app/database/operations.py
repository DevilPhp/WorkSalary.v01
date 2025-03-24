from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey, DateTime, Boolean, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base, SessionLocal

modelOperationsType = Table(
    'modelOperationsTypes',
    Base.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('ModelOpID', Integer, ForeignKey('operations.ОперацияNo'), primary_key=True),
    Column('OpTypeID', Integer, ForeignKey('operationTypes.OperTypeID'), nullable=True)
)

class Operation(Base):
    __tablename__ = 'operations'
    ОперацияNo = Column(Integer, primary_key=True)
    Операция = Column(String, nullable=True)

    operationTypes = relationship('OperationType', secondary='modelOperationsTypes', back_populates='operations')


