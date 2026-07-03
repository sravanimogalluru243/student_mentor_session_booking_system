from pydantic import BaseModel, EmailStr
from typing import Optional


class StudentBase(BaseModel):
    name: str
    email: EmailStr


class StudentCreate(StudentBase):
    password: str


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None


class StudentRead(StudentBase):
    id: int

    class Config:
        from_attributes = True


class PasswordChangeRequest(BaseModel):
    old_password: str
    new_password: str
