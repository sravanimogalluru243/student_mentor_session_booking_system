from sqlalchemy import Column, Integer, ForeignKey, String, Time
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Availability(Base):
    __tablename__ = "availability"

    id = Column(Integer, primary_key=True, index=True)

    mentor_id = Column(
        Integer,
        ForeignKey("mentors.id", ondelete="CASCADE")
    )

    day = Column(String(20))

    start_time = Column(Time)

    end_time = Column(Time)

    mentor = relationship(
        "Mentor",
        back_populates="availabilities"
    )