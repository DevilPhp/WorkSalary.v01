from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey, DateTime, Boolean, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

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
    productionModelOperations = relationship('ProductionModelOperations', back_populates='operations')


class DefaultOperForVidObleklo(Base):
    __tablename__ = 'defaultOperForVidOblekla'
    id = Column(Integer, primary_key=True, autoincrement=True)
    OblekloVid = Column(Integer, ForeignKey('vidOblekla.OblekloVid'), primary_key=True)
    ОперацияNo = Column(Integer, ForeignKey('operations.ОперацияNo'), primary_key=True)
    defaultTime = Column(Float, default=0)

    operations = relationship('Operation', back_populates='defaultOperForVidOblekla')
    vidOblekla = relationship('VidObleklo', back_populates='defaultOperForVidOblekla')


class ProductionModelOperations(Base):
    __tablename__ = "productionModelOperations"
    id = Column(Integer, primary_key=True)
    OrderId = Column(Integer, ForeignKey("productionModels.id"), nullable=True)
    ПоръчкаNo = Column(String, index=True)
    ОперацияNo = Column(Integer, ForeignKey("operations.ОперацияNo"), nullable=True)
    Операция = Column(String, nullable=False)
    TimeForOper = Column(Float, default=0)
    Razcenka = Column(Float, default=0)
    LastUpdated = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    UpdatedBy = Column(String, default="System")

    productionModel = relationship("ProductionModel", back_populates="productionModelOperations")
    operations = relationship("Operation", back_populates="productionModelOperations")
    timePaperOperations = relationship("TimePaperOperation", back_populates="productionModelOperations")
