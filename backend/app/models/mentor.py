from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Mentor(Base):
    __tablename__ = "mentors"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    specialization = Column(String(100))
    experience = Column(Integer)
    bio = Column(String(500))

    bookings = relationship(
        "Booking",
        back_populates="mentor",
        cascade="all, delete"
    )

    feedbacks = relationship(
        "Feedback",
        back_populates="mentor",
        cascade="all, delete"
    )

    availabilities = relationship(
        "Availability",
        back_populates="mentor",
        cascade="all, delete"
    )