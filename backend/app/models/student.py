from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    course = Column(String(100))
    phone = Column(String(20))

    bookings = relationship(
        "Booking",
        back_populates="student",
        cascade="all, delete"
    )

    feedbacks = relationship(
        "Feedback",
        back_populates="student",
        cascade="all, delete"
    )

