from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Feedback(Base):
    __tablename__ = "feedback"

    id = Column(Integer, primary_key=True, index=True)

    booking_id = Column(
        Integer,
        ForeignKey("bookings.id", ondelete="CASCADE"),
        unique=True
    )

    student_id = Column(
        Integer,
        ForeignKey("students.id", ondelete="CASCADE")
    )

    mentor_id = Column(
        Integer,
        ForeignKey("mentors.id", ondelete="CASCADE")
    )

    rating = Column(Integer)

    comment = Column(Text)

    booking = relationship(
        "Booking",
        back_populates="feedback"
    )

    student = relationship(
        "Student",
        back_populates="feedbacks"
    )

    mentor = relationship(
        "Mentor",
        back_populates="feedbacks"
    )

    