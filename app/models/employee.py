from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Employee(Base):
    __tablename__ = "hrms_employees"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, unique=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    department = Column(String, nullable=False)