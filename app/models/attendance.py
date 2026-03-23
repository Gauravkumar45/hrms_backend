from sqlalchemy import Column, Integer, String, Date, ForeignKey
from app.db.database import Base

class Attendance(Base):
    __tablename__ = "hrms_attendance"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, ForeignKey("hrms_employees.employee_id"))
    date = Column(Date)
    status = Column(String)