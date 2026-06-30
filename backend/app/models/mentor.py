from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Mentor(Base):
    __tablename__ = "mentors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    expertise = Column(String, nullable=True)
    bio = Column(Text, nullable=True)

    sessions = relationship("Session", back_populates="mentor")
    feedbacks = relationship("Feedback", back_populates="mentor")
