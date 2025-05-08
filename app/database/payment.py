from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey, DateTime, Boolean, Table, Date
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class PaymentPerMinute(Base):
    __tablename__ = 'paymentPerMinutes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    PaymentValue = Column(Float, nullable=False)
    PaymentInEuro = Column(Float, nullable=False)
    DateActive = Column(Date, nullable=True)
    Comment = Column(String(255), nullable=True)
    LastUpdated = Column(Date, default=datetime.now, onupdate=datetime.now)
    UpdatedBy = Column(String(255), nullable=True)


class NightPaymentPerMinute(Base):
    __tablename__ = 'nightPaymentPerMinutes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    NightPaymentValue = Column(Float, nullable=False)
    NightPaymentInEuro = Column(Float, nullable=False)
    DateActive = Column(Date, nullable=True)
    Comment = Column(String(255), nullable=True)
    LastUpdated = Column(Date, default=datetime.now, onupdate=datetime.now)
    UpdatedBy = Column(String(255), nullable=True)


class PaymentCurrency(Base):
    __tablename__ = 'paymentCurrencies'
    id = Column(Integer, primary_key=True, autoincrement=True)
    CurrencyName = Column(String(50), nullable=False, unique=True)
    CurrencySymbol = Column(String(10), nullable=False, unique=True)
    ConversionRateFromLev = Column(Float, nullable=False)
    ConversionRateFromEuro = Column(Float, nullable=False)
    LastUpdated = Column(Date, default=datetime.now, onupdate=datetime.now)
    UpdatedBy = Column(String, nullable=True)
