from app.logger import logger
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager
from config import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    pool_size=10,         # Allow up to 10 connections at a time
    max_overflow=5,       # Allow up to 5 extra connections if needed
    pool_timeout=30,      # Wait time before throwing timeout error
    pool_recycle=1800,    # Recycle connections every 30 minutes
    echo=False            # Disable debug logs for production
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Context manager approach
@contextmanager
def getDatabase():
    """Context manager for database sessions"""
    session = SessionLocal()
    try:
        yield session
        # session.commit()
    except Exception as e:
        logger.error(f'Error: {e}')
        raise e
    finally:
        session.close()

@contextmanager
def setDatabase():
    session = SessionLocal()
    try:
        yield session
        session.commit()

    except Exception as e:
        logger.error(f'Error: {e}')
        session.rollback()
        raise e
    finally:
        session.close()
        logger.info('Session closed')

# def getDatabase():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


def createTable():
    from app.database.users import User
    from app.database.workers import Worker, Cehove
    from app.database.models import VidObleklo, Client, Yarn, ProductionModel
    from app.database.operations import Operation, modelOperationsType, DefaultOperForVidObleklo, ProductionModelOperations
    from app.database.workers import TimePaperOperation, TimePaper
    from app.database.payment import PaymentPerMinute

    Base.metadata.create_all(bind=engine)
    createDefaultPaymentTypes()
    createDefaultCurrency()


def createDefaultPaymentTypes():
    from app.database.workers import PaymentType
    db = SessionLocal()
    paymentTypes = ['Няма', 'Повременна', 'Сделна', 'Щатна', 'Майки', 'Други', 'Напуснали']
    try:
        existingPaymentTypes = db.query(PaymentType).all()
        if len(existingPaymentTypes) != 0:
            return
        count = 0
        for paymentType in paymentTypes:
            newPaymentType = PaymentType(id=count, Name=paymentType)
            db.add(newPaymentType)
            count += 1
        db.commit()
        print("Default payment types created successfully.")
        return
    except Exception as e:
        print(f"Error creating default payment types: {e}")
        db.rollback()
    finally:
        db.close()


def createDefaultCurrency():
    from app.database.payment import PaymentCurrency
    db = SessionLocal()
    try:
        existingCurrency = db.query(PaymentCurrency).first()
        if existingCurrency:
            return
        newCurrency = PaymentCurrency(
            CurrencyName='Euro',
            CurrencySymbol='EUR',
            ConversionRateFromLev=1.95583,
            ConversionRateFromEuro=1,
            UpdatedBy='system'
        )
        db.add(newCurrency)
        db.commit()
        print("Default currency created successfully.")
        return
    except Exception as e:
        print(f"Error creating default currency: {e}")
        db.rollback()
    finally:
        db.close()
