from sqlalchemy import Column, Integer, ForeignKey, Date, Time, String
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(
        Integer,
        ForeignKey("students.id", ondelete="CASCADE")
    )

    mentor_id = Column(
        Integer,
        ForeignKey("mentors.id", ondelete="CASCADE")
    )

    booking_date = Column(Date, nullable=False)
    booking_time = Column(Time, nullable=False)

    status = Column(String(20), default="Pending")
    attendance = Column(String(20), nullable=True)

    student = relationship(
        "Student",
        back_populates="bookings"
    )

    mentor = relationship(
        "Mentor",
        back_populates="bookings"
    )

    session = relationship(
        "Session",
        back_populates="booking",
        uselist=False
    )

    feedback = relationship(
        "Feedback",
        back_populates="booking",
        uselist=False
    )