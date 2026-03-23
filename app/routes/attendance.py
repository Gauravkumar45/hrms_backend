from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.attendance import Attendance
from app.models.employee import Employee
from app.schemas.attendance import AttendanceCreate, AttendanceResponse
from app.db.db_config import get_db

router = APIRouter(prefix="/attendance", tags=["Attendance"])

@router.post("/", response_model=dict)
def mark_attendance(data: AttendanceCreate, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(
        Employee.employee_id == data.employee_id
    ).first()

    if not emp:
        raise HTTPException(
            status_code=404,
            detail="Employee not found"
        )
    existing = db.query(Attendance).filter(
        Attendance.employee_id == data.employee_id,
        Attendance.date == data.date
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Attendance already marked for this date. Use update endpoint to modify."
        )

    attendance = Attendance(**data.dict())
    db.add(attendance)
    db.commit()
    return {"message": "Attendance marked successfully. Use {employee_id} to view records."}

@router.get("/{employee_id}", response_model=list[AttendanceResponse])
def get_attendance(employee_id: str, db: Session = Depends(get_db)):
    records = db.query(Attendance).filter(
        Attendance.employee_id == employee_id
    ).all()
    return records


@router.get("/summary/{employee_id}")
def attendance_summary(employee_id: str, db: Session = Depends(get_db)):
    records = db.query(Attendance).filter(
        Attendance.employee_id == employee_id
    ).all()
    total_present = sum(
        1 for r in records if r.status.strip().lower() == "present"
    )
    return {
        "employee_id": employee_id,
        "total_present_days": total_present
    }