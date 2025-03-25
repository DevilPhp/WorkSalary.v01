from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base, SessionLocal


class VidObleklo(Base):
    __tablename__ = "vidOblekla"
    OblekloVid = Column(Integer, primary_key=True)
    OblekloName = Column(String, nullable=True)

    defaultOperForVidOblekla = relationship("DefaultOperForVidObleklo", back_populates="vidOblekla")
    productionModel = relationship("ProductionModel", back_populates="vidOblekla")


class Client(Base):
    __tablename__ = "clients"
    ClientID = Column(Integer, primary_key=True)
    Клиент = Column(String, nullable=True)

    productionModel = relationship("ProductionModel", back_populates="client")

class Yarn(Base):
    __tablename__ = "yarns"
    YarnID = Column(Integer, primary_key=True)
    ПреждаТип = Column(String, nullable=True)
    Състав = Column(String, nullable=True)
    Доставчик = Column(String, nullable=True)

    productionModel = relationship("ProductionModel", back_populates="yarn")


class ProductionModel(Base):
    __tablename__ = "productionModels"
    id = Column(Integer, primary_key=True, autoincrement=True)
    ПоръчкаNo = Column(String, nullable=True, index=True)
    Descr = Column(String, nullable=True, default=None)
    Actual = Column(Boolean, default=True)
    ClientID = Column(Integer, ForeignKey("clients.ClientID"), nullable=True)
    Fain = Column(String, nullable=True)
    WearType = Column(Integer, ForeignKey("vidOblekla.OblekloVid"), nullable=True)
    YarnType = Column(Integer, ForeignKey("yarns.YarnID"), nullable=True)
    Броя = Column(Integer, default=0)
    DateCreated = Column(DateTime, default=datetime.now)
    TargetDate = Column(DateTime, nullable=True, default=None)
    Status = Column(String, nullable=True, default=None)
    UserCreated = Column(String, nullable=False)

    client = relationship("Client", back_populates="productionModel")
    vidOblekla = relationship("VidObleklo", back_populates="productionModel")
    yarn = relationship("Yarn", back_populates="productionModel")

