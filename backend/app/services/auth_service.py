from datetime import datetime, timedelta
from typing import Optional

from jose import jwt
from passlib.context import CryptContext

from app.models.student import Student
from app.schemas.student import StudentCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "change-me-in-production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_student(db, student_in: StudentCreate) -> Student:
    student = Student(
        name=student_in.name,
        email=student_in.email,
        hashed_password=get_password_hash(student_in.password),
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def authenticate_student(db, email: str, password: str) -> Optional[Student]:
    student = db.query(Student).filter(Student.email == email).first()
    if not student:
        return None
    if not verify_password(password, student.hashed_password):
        return None
    return student


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
