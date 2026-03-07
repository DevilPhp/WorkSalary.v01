"""
app/database/mobile_accounts.py

New table for mobile worker authentication.
Add this import to app/database/__init__.py inside createTable():
    from app.database import mobile_accounts
"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class MobileWorkerAccount(Base):
    __tablename__ = "mobileWorkerAccounts"

    id            = Column(Integer, primary_key=True, autoincrement=True)
    WorkerNo      = Column(Integer, ForeignKey("workers.Номер"), unique=True, nullable=False)
    PlainPassword = Column(String, nullable=False)   # Visible to admin for password recovery
    PasswordHash  = Column(String, nullable=False)   # Used for actual authentication
    DeviceId      = Column(String, nullable=True)    # Browser fingerprint (replaces IMEI)
    RegisteredAt  = Column(DateTime, default=datetime.now)
    UpdatedAt     = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    worker = relationship("Worker", backref="mobileAccount")
