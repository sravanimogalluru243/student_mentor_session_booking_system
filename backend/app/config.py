import os
from functools import lru_cache
from pathlib import Path

from dotenv import load_dotenv


env_path = Path(__file__).resolve().parents[1] / ".env"
load_dotenv(env_path)


class Settings:
    def __init__(self):
        self.app_name = os.getenv("APP_NAME", "Student Mentor Booking")
        self.database_url = os.getenv(
            "DATABASE_URL",
            "postgresql://postgres:123456789@localhost:5432/student_mentor_db",
        )
        self.secret_key = os.getenv("SECRET_KEY", "change-me-in-production")
        self.algorithm = os.getenv("ALGORITHM", "HS256")
        self.access_token_expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))


@lru_cache()
def get_settings() -> Settings:
    return Settings()
