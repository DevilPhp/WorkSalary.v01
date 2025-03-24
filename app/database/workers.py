from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship

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

