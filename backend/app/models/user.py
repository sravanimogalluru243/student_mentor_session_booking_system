from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
import enum

from app.database.connection import Base


class UserRole(str, enum.Enum):
    admin = "admin"
    mentor = "mentor"
    student = "student"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), nullable=False)

    student_profile = relationship(
        "Student",
        back_populates="user",
        uselist=False,
        cascade="all, delete"
    )

    mentor_profile = relationship(
        "Mentor",
        back_populates="user",
        uselist=False,
        cascade="all, delete"
    )