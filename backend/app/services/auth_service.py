from datetime import datetime, timedelta
from typing import Optional

from fastapi import HTTPException
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.config import get_settings
from app.models.admin import Admin
from app.models.mentor import Mentor
from app.models.student import Student
from app.schemas.student import StudentCreate


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    settings = get_settings()
    expire = datetime.utcnow() + (
        expires_delta or timedelta(minutes=settings.access_token_expire_minutes)
    )
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)


def register_student(db: Session, student_in: StudentCreate) -> Student:
    existing = db.query(Student).filter(Student.email == student_in.email).first()
    if existing:
        raise HTTPException(status_code=409, detail="Student email already registered")

    student = Student(
        full_name=student_in.full_name,
        email=student_in.email,
        password=get_password_hash(student_in.password),
        course=student_in.course,
        phone=student_in.phone,
    )
    db.add(student)
    db.commit()
    db.refresh(student)
    return student


def authenticate_student(db: Session, email: str, password: str) -> Optional[Student]:
    return _authenticate(db, Student, email, password)


def authenticate_mentor(db: Session, email: str, password: str) -> Optional[Mentor]:
    return _authenticate(db, Mentor, email, password)


def authenticate_admin(db: Session, email: str, password: str) -> Optional[Admin]:
    return _authenticate(db, Admin, email, password)


def _authenticate(db: Session, model, email: str, password: str):
    user = db.query(model).filter(model.email == email).first()
    if not user or not verify_password(password, user.password):
        return None
    return user
