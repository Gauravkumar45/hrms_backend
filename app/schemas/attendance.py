from pydantic import BaseModel
from datetime import date
from app.enum.attendance_enum import StatusEnum

class AttendanceCreate(BaseModel):
    employee_id: str
    date: date
    status: StatusEnum

class AttendanceResponse(BaseModel):
    employee_id: str
    date: date
    status: StatusEnum

    class Config:
        from_attributes = True