from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey, DateTime, Boolean, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class PaymentPerMinute(Base):
    __tablename__ = 'paymentPerMinutes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    PaymentValue = Column(Float, nullable=False)
    PaymentInEuro = Column(Float, nullable=False)
    LevToEuro = Column(Float, default=1.95584, nullable=False)
    DateActive = Column(DateTime, nullable=True)
    Comment = Column(String(255), nullable=True)
    LastUpdated = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    UpdatedBy = Column(String(255), nullable=True)
