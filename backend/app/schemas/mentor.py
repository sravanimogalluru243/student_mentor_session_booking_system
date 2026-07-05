from datetime import time
from typing import Optional

from pydantic import BaseModel, EmailStr


class AvailabilityCreate(BaseModel):
    day: str
    start_time: time
    end_time: time


class AvailabilityRead(AvailabilityCreate):
    id: int

    class Config:
        from_attributes = True


class MentorCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    specialization: Optional[str] = None
    experience: Optional[int] = None
    bio: Optional[str] = None


class MentorUpdate(BaseModel):
    full_name: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    specialization: Optional[str] = None
    experience: Optional[int] = None
    bio: Optional[str] = None


class MentorRead(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    specialization: Optional[str] = None
    experience: Optional[int] = None
    bio: Optional[str] = None
    availabilities: list[AvailabilityRead] = []

    class Config:
        from_attributes = True
