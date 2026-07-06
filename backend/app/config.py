import os
from functools import lru_cache


class Settings:
    def __init__(self):
        self.app_name = os.getenv("APP_NAME", "Student Mentor Booking")
        self.database_url = os.getenv(
            "DATABASE_URL",
<<<<<<< HEAD
            "postgresql://postgres:admin123@localhost:5432/student_mentor_db",
=======
            "postgresql://postgres:123456@localhost:5432/student_mentor_db",
>>>>>>> dcf91507ea54de3297742562edd421d9e2455480
        )
        self.secret_key = os.getenv("SECRET_KEY", "change-me-in-production")
        self.algorithm = os.getenv("ALGORITHM", "HS256")
        self.access_token_expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))


@lru_cache()
def get_settings() -> Settings:
    return Settings()
