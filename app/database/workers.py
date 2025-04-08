from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey, DateTime, Boolean, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base, SessionLocal


class Worker(Base):
    __tablename__ = "workers"
    Номер = Column(Integer, primary_key=True, index=True)
    Име = Column(String, nullable=True)
    Презиме = Column(String, nullable=True)
    Фамилия = Column(String, nullable=True)
    Група = Column(Integer, ForeignKey("cehove.id"), nullable=True)
    Длъжност = Column(Integer, ForeignKey("workerPositions.ДлъжностКод"), nullable=True)
    Коефициент = Column(Float, nullable=True)
    ЕГН = Column(String, nullable=True)
    КасаКод = Column(Integer, autoincrement=True)
    ДатаНаПостъпване = Column(DateTime, nullable=True)
    ДатаНаНапускане = Column(DateTime, nullable=True)
    СистемаЗаплащане = Column(Integer, ForeignKey("paymentTypes.id"), default=0)
    гр_с = Column(String, nullable=True)
    Адрес = Column(String, nullable=True)
    Телефон = Column(String, nullable=True)
    ТрудовСтажГодини = Column(Integer, nullable=True)
    ТрудовСтажМесеци = Column(Integer, nullable=True)
    ТрудовСтажДни = Column(Integer, nullable=True)
    ДатаНачалоТрудСтаж = Column(DateTime, nullable=True)

    cehove = relationship("Cehove", back_populates="workers")
    workerPosition = relationship("WorkerPosition", back_populates="workers")
    paymentType = relationship("PaymentType", back_populates="workers")
    timePaper = relationship("TimePaper", back_populates="worker")


class PaymentType(Base):
    __tablename__ = "paymentTypes"
    id = Column(Integer, primary_key=True)
    Name = Column(String, nullable=True)

    workers = relationship("Worker", back_populates="paymentType")


class Cehove(Base):
    __tablename__ = "cehove"
    id = Column(Integer, primary_key=True)
    Група = Column(String, nullable=True)
    ГрупаName = Column(String, nullable=True)
    Вид = Column(String, nullable=True)
    SupervisorNo = Column(Integer, nullable=True)

    workers = relationship("Worker", back_populates="cehove")


class WorkerPosition(Base):
    __tablename__ = "workerPositions"
    # id = Column(Integer, primary_key=True)
    ДлъжностКод = Column(Integer, primary_key=True)
    Длъжност = Column(String, nullable=True)
    Коефициент = Column(Float, nullable=True)
    ВидОперация = Column(Integer, ForeignKey("operationTypes.OperTypeID"), nullable=True)

    operationType = relationship("OperationType", back_populates="workerPositions")
    workers = relationship("Worker", back_populates="workerPosition")


class OperationType(Base):
    __tablename__ = "operationTypes"
    OperTypeID = Column(Integer, primary_key=True)
    OperName = Column(String, nullable=True)

    workerPositions = relationship("WorkerPosition", back_populates="operationType")
    operations = relationship("Operation", secondary='modelOperationsTypes', back_populates="operationTypes")


class TimePaper(Base):
    __tablename__ = "timePapers"
    id = Column(Integer, primary_key=True)
    Date = Column(DateTime, nullable=False)
    ShiftId = Column(Integer, ForeignKey('workingShifts.id'), nullable=True)
    IsHourlyPaid = Column(Integer, ForeignKey('hourlyPays.id'), nullable=True)
    IsOvertime = Column(Integer, ForeignKey('overtimePays.id'), nullable=True)
    WorkerId = Column(Integer, ForeignKey('workers.Номер'), nullable=False)
    OrderId = Column(Integer, ForeignKey('productionModels.id'), nullable=True)
    modelOperationsId = Column(Integer, ForeignKey('timePaperOperations.id'), nullable=True)

    shift = relationship("WorkingShift", back_populates="timePaper")
    isHourlyPaid = relationship("HourlyPay", back_populates="timePaper")
    isOvertime = relationship("OvertimePay", back_populates="timePaper")
    worker = relationship("Worker", back_populates="timePaper")
    productionModel = relationship("ProductionModel", back_populates="timePaper")
    timePaperOperation = relationship("TimePaperOperation", back_populates="timePaper")


class TimePaperOperation(Base):
    __tablename__ = 'timePaperOperations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    TimePaperId = Column(Integer, ForeignKey('timePapers.id'), nullable=False),
    ModelOperationId = Column(Integer, ForeignKey('productionModelOperations.id'), nullable=True)
    Pieces = Column(Integer, nullable=False, default=0)
    WorkingTime = Column(Float, nullable=False, default=0)

    timePaper = relationship("TimePaper", back_populates="timePaperOperation")
    modelOperation = relationship("ProductionModelOperation", back_populates="timePaperOperation")

class WorkingShift(Base):
    __tablename__ = "workingShifts"
    id = Column(Integer, primary_key=True)
    ShiftName = Column(String, nullable=True)
    StartTime = Column(DateTime, nullable=False)
    EndTime = Column(DateTime, nullable=False)
    BreakTime = Column(Integer, nullable=True, default=30)
    Efficiency = Column(Float, nullable=False)
    DateUpdated = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    UserUpdated = Column(String, nullable=False)

    timePaper = relationship("TimePaper", back_populates="shift")


class HourlyPay(Base):
    __tablename__ = "hourlyPays"
    id = Column(Integer, primary_key=True)
    Start = Column(DateTime, nullable=False)
    End = Column(DateTime, nullable=False)
    Efficiency = Column(Float, nullable=False)
    HourlyRate = Column(Float, nullable=False)
    # TimePaperId = Column(Integer, ForeignKey('timePapers.id'))
    DateUpdated = Column(DateTime, nullable=False, default=datetime.now)
    UserUpdated = Column(String, nullable=False)

    timePaper = relationship("TimePaper", back_populates="isHourlyPaid")


class OvertimePay(Base):
    __tablename__ = "overtimePays"
    id = Column(Integer, primary_key=True)
    Start = Column(DateTime, nullable=False)
    End = Column(DateTime, nullable=False)
    Efficiency = Column(Float, nullable=False)
    OvertimeRate = Column(Float, nullable=False)
    # TimePaperId = Column(Integer, ForeignKey('timePapers.id'), nullable=True)
    DateUpdated = Column(DateTime, nullable=False, default=datetime.now)
    UserUpdated = Column(String, nullable=False)

    timePaper = relationship("TimePaper", back_populates="isOvertime")
