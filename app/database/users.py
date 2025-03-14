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


def createUser(username, password, role=None):
    try:
        hashedPassword = encrypt.hash(password)
        user = User(username=username, passwordHash=hashedPassword, userRole=role)
        session.add(user)
        session.commit()
        return {"message": "User created successfully"}
    except Exception as e:
        session.rollback()
        return {"error": str(e)}
    finally:
        session.close()
