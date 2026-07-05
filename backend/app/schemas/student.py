from typing import Optional

from pydantic import BaseModel, EmailStr


class StudentCreate(BaseModel):
    full_name: str
    email: EmailStr
    course: Optional[str] = None
    phone: Optional[str] = None
    password: str


class StudentUpdate(BaseModel):
    full_name: Optional[str] = None
    course: Optional[str] = None
    phone: Optional[str] = None
    password: Optional[str] = None


class StudentRead(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    course: Optional[str] = None
    phone: Optional[str] = None

    class Config:
        from_attributes = True
