from sqlalchemy import Column, Integer, String, Float, Enum
from app.database import Base, SessionLocal
from passlib.hash import pbkdf2_sha256 as encrypt

session = SessionLocal()


class UserRole(str, Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    OPERATOR = "operator"
    GUEST = "guest"


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    passwordHash = Column(String(255), nullable=False)
    userRole = Column(String(), default='Guest', nullable=False)
