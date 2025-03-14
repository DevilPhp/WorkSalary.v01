from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL

engine = create_engine(
    DATABASE_URL,
    pool_size=10,         # Allow up to 10 connections at a time
    max_overflow=5,       # Allow up to 5 extra connections if needed
    pool_timeout=30,      # Wait time before throwing timeout error
    pool_recycle=1800,    # Recycle connections every 30 minutes
    echo=True            # Disable debug logs for production
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def getDatabase():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def createTable():
    from app.database.users import User
    Base.metadata.create_all(bind=engine)