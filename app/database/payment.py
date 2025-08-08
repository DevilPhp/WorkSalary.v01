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


class HolidaysPerYear(Base):
    __tablename__ = 'holidaysPerYears'
    id = Column(Integer, primary_key=True, autoincrement=True)
    Year = Column(Integer, nullable=False, unique=True)
    HolidaysCount = Column(Integer, nullable=False)
    LastUpdated = Column(Date, default=datetime.now, onupdate=datetime.now)
    UpdatedBy = Column(String, nullable=True)

    holidays = relationship("Holiday", back_populates="holidaysPerYears")


class Holiday(Base):
    __tablename__ = 'holidays'
    id = Column(Integer, primary_key=True, autoincrement=True)
    HolidayDate = Column(Date, nullable=False)
    HolidayName = Column(String(255), nullable=False)
    HolidaysPerYearId = Column(Integer, ForeignKey('holidaysPerYears.id'))
    LastUpdated = Column(Date, default=datetime.now, onupdate=datetime.now)
    UpdatedBy = Column(String, nullable=True)

    holidaysPerYears = relationship("HolidaysPerYear", back_populates="holidays")


class PaymentsRates(Base):
    __tablename__ = 'paymentsRates'
    id = Column(Integer, primary_key=True, autoincrement=True)
    RateType = Column(String(255), nullable=False, unique=True)
    RateValue = Column(Float, nullable=False)
    RateValueInEuro = Column(Float, nullable=False)
    RatePercentage = Column(Float, nullable=False)
    LastUpdated = Column(Date, default=datetime.now, onupdate=datetime.now)
    UpdatedBy = Column(String, nullable=True)
