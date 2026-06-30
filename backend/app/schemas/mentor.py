from pydantic import BaseModel, EmailStr
from typing import Optional


class MentorBase(BaseModel):
    name: str
    email: EmailStr
    expertise: Optional[str] = None
    bio: Optional[str] = None


class MentorCreate(MentorBase):
    password: str


class MentorRead(MentorBase):
    id: int

    class Config:
        from_attributes = True
