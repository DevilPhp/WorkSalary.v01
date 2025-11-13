import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_SERVER', 'localhost')
DB_PORT = os.getenv('DB_PORT', 5400)
DB_NAME = os.getenv('DB_NAME', 'knitex')
DB_SERVER_PORT = os.getenv('DB_SERVER_PORT', 6000)

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
API_SERVER = f"http://{DB_HOST}:{DB_SERVER_PORT}/api"

SECRET_LOGIN = os.getenv('SECRET_LOGIN')
