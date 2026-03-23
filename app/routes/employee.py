from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeResponse
from app.db.db_config import get_db

router = APIRouter(prefix="/employees", tags=["Employees"])

@router.post("/")
def create_employee(data: EmployeeCreate, db: Session = Depends(get_db)):
    existing = db.query(Employee).filter(
        (Employee.email == data.email) |
        (Employee.employee_id == data.employee_id)
    ).first()

    if existing:
        raise HTTPException(status_code=400, detail="Employee already exists with this email or employee ID")

    emp = Employee(**data.dict())
    db.add(emp)
    db.commit()
    db.refresh(emp)
    return emp

@router.get("/", response_model=list[EmployeeResponse])
def list_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()

@router.delete("/{employee_id}")
def delete_employee(employee_id: str, db: Session = Depends(get_db)):
    emp = db.query(Employee).filter(Employee.employee_id == employee_id).first()

    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(emp)
    db.commit()
    return {"message": "Employee deleted successfully."}