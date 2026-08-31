from sqlalchemy import Column, Integer, String, Date
from .database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    roll_number = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    phone = Column(String(20), nullable=False)
    date_of_birth = Column(Date, nullable=True)
    department = Column(String(100), nullable=False)
    year = Column(Integer, nullable=False)
    address = Column(String(255), nullable=True)
    city = Column(String(100), nullable=True)
    nativeplace = Column(String(100), nullable=True)
    tenth_mark = Column(Integer, nullable=True)
    twelfth_mark = Column(Integer, nullable=True)