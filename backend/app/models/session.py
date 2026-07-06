from sqlalchemy import Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Session(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)

    booking_id = Column(
        Integer,
        ForeignKey("bookings.id", ondelete="CASCADE"),
        unique=True
    )

    start_time = Column(DateTime)

    end_time = Column(DateTime)

    status = Column(String(20), default="Scheduled")

    booking = relationship(
        "Booking",
        back_populates="session"
    )