from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional


class StudentBase(BaseModel):
    full_name: str
    roll_number: str
    email: EmailStr
    phone: str
    date_of_birth: Optional[date] = None
    department: str
    year: int
    address: Optional[str] = None
    city: Optional[str] = None
    nativeplace: Optional[str] = None

class StudentCreate(StudentBase):
    pass


class StudentUpdate(StudentBase):
    pass


class StudentOut(StudentBase):
    id: int

    class Config:
        from_attributes = True
