import os
from dotenv import load_dotenv


load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")

    JWT_SECRET = os.getenv("JWT_SECRET")
    JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    SMTP_SERVER = os.getenv("SMTP_SERVER")
    SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
    SMTP_USER = os.getenv("SMTP_USER")
    SMTP_PASS = os.getenv("SMTP_PASS")

    GRAPH_MODEL_PATH = os.getenv("GRAPH_MODEL_PATH")
    ML_MODEL_PATH = os.getenv("ML_MODEL_PATH")

    DEBUG_MODE = os.getenv("DEBUG_MODE") == "True"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "info")

settings = Settings()

# print("Database URL:", Settings.DATABASE_URL)
# print("JWT Secret:", Settings.JWT_SECRET)
# print("SMTP Server:", Settings.SMTP_SERVER)