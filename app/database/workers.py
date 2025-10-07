from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey, DateTime, Boolean, Table, Time, Date
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base, SessionLocal
# from app.database.operations import ProductionModelOperations


class Worker(Base):
    __tablename__ = "workers"
    Номер = Column(Integer, primary_key=True, index=True, autoincrement=True)
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
    timePapers = relationship("TimePaper", back_populates="workers")


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
    Date = Column(Date, nullable=False)
    WeekDay = Column(Integer)
    PaymentRatio = Column(Float, default=1)
    ShiftId = Column(Integer, ForeignKey('workingShifts.id'), nullable=True)
    # IsHourlyPaid = Column(Integer, ForeignKey('hourlyPays.id'), nullable=True)
    # IsOvertime = Column(Integer, ForeignKey('overtimePays.id'), nullable=True, default=None)
    NightShiftMins = Column(Integer, nullable=True)
    WorkerId = Column(Integer, ForeignKey('workers.Номер'), nullable=False)
    TotalPieces = Column(Integer, nullable=False, default=0)
    TotalHours = Column(Float, nullable=False, default=0)
    userCreated = Column(String, nullable=False)

    # modelOperationsId = Column(Integer, ForeignKey('timePaperOperations.id'), nullable=True)

    workingShifts = relationship("WorkingShift", back_populates="timePapers")
    hourlyPays = relationship("HourlyPay", back_populates="timePapers")
    overtimePays = relationship("OvertimePay", back_populates="timePapers")
    workers = relationship("Worker", back_populates="timePapers")
    timePaperOperations = relationship("TimePaperOperation", back_populates="timePaper")


class TimePaperOperation(Base):
    __tablename__ = 'timePaperOperations'
    id = Column(Integer, primary_key=True, autoincrement=True)
    TimePaperId = Column(Integer, ForeignKey('timePapers.id'), nullable=False)
    OrderId = Column(Integer, ForeignKey('productionModels.id'), nullable=True)
    ModelOperationId = Column(Integer, ForeignKey('productionModelOperations.id'), nullable=True)
    Pieces = Column(Integer, nullable=False, default=0)
    WorkingTimeMinutes = Column(Float, nullable=False, default=0)

    timePaper = relationship("TimePaper", back_populates="timePaperOperations")
    productionModels = relationship("ProductionModel", back_populates="timePaperOperations")
    productionModelOperations = relationship("ProductionModelOperations", back_populates="timePaperOperations")


class WorkingShift(Base):
    __tablename__ = "workingShifts"
    id = Column(Integer, primary_key=True)
    ShiftName = Column(String, nullable=True)
    StartTime = Column(Time, nullable=False)
    EndTime = Column(Time, nullable=False)
    BreakTime = Column(Integer, nullable=True, default=60)
    Efficiency = Column(Float, nullable=False)
    DateUpdated = Column(Date, nullable=False, default=datetime.today(), onupdate=datetime.today())
    UserUpdated = Column(String, nullable=False)

    timePapers = relationship("TimePaper", back_populates="workingShifts")


class HourlyPay(Base):
    __tablename__ = "hourlyPays"
    id = Column(Integer, primary_key=True)
    TimePaperId = Column(Integer, ForeignKey('timePapers.id'), nullable=False)
    Start = Column(Time, nullable=False)
    End = Column(Time, nullable=False)
    Efficiency = Column(Float, nullable=False)
    HourlyRate = Column(Float, nullable=False, default=1)
    DateUpdated = Column(Date, nullable=False, default=datetime.today(), onupdate=datetime.today())
    UserUpdated = Column(String, nullable=False)

    timePapers = relationship("TimePaper", back_populates="hourlyPays")


class OvertimePay(Base):
    __tablename__ = "overtimePays"
    id = Column(Integer, primary_key=True)
    TimePaperId = Column(Integer, ForeignKey('timePapers.id'), nullable=False)
    Start = Column(Time, nullable=False)
    End = Column(Time, nullable=False)
    Efficiency = Column(Float, nullable=False)
    OvertimeRate = Column(Float, nullable=False, default=1.5)
    DateUpdated = Column(Date, nullable=False, default=datetime.today(), onupdate=datetime.today())
    UserUpdated = Column(String, nullable=False)

    timePapers = relationship("TimePaper", back_populates="overtimePays")
