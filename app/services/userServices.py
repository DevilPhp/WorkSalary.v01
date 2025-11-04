from app.logger import logger
from app.database import getDatabase, setDatabase
from app.database.users import User
from passlib.hash import pbkdf2_sha256 as encrypt


class UserServices:

    @staticmethod
    def registerNewUser(data):
        with setDatabase() as session:
            username = data.get('Потребител')
            password = data.get('Парола')
            role = data.get('Ниво').lower() if data.get('Ниво') else 'guest'
            hashedPassword = encrypt.hash(password)

            if session.query(User).filter_by(username=username).first():
                logger.error(f"User {username} already exists")
                return -1
            else:
                user = User(username=username, passwordHash=hashedPassword, userRole=role)
                session.add(user)
                session.commit()
                if user:
                    logger.info(f"User {username} has been registered successfully")
                    return 1
                else:
                    logger.error("Failed to register user")
                    return 0

    @staticmethod
    def deleteUser(rowId):
        with setDatabase() as session:
            user = session.query(User).get(int(rowId))
            if user:
                session.delete(user)
                session.commit()
                logger.info(f"User with ID {user.id} - {user.username} has been deleted successfully")
                return True
            else:
                logger.error(f"User with ID {user.id} - {user.username} does not exist")
                return False

    @staticmethod
    def loginUser(username, password):
        with getDatabase() as session:
            user = session.query(User).filter_by(username=username).first()
            if not user:
                logger.error(f"User {username} does not exist")
                return False
            if encrypt.verify(password, user.passwordHash):
                logger.info(f"User {username} has logged in successfully")
                return True
            else:
                logger.error(f"Invalid username or password for user {username}")
                return False

    @staticmethod
    def updateUser(username, new_password, rol):
        pass