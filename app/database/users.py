from sqlalchemy import Column, Integer, String, Float, Enum
from app.database import Base, getDatabase
from passlib.hash import bcrypt


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


def createUser(username, password, role=None):
    try:
        db = getDatabase()
        hashedPassword = bcrypt.hash(password)
        user = User(username=username, passwordHash=hashedPassword, userRole=role)
        db.session.add(user)
        db.session.commit()
        return {"message": "User created successfully"}
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}
