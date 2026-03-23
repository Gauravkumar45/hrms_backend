from pydantic import BaseModel, EmailStr

class EmployeeCreate(BaseModel):
    employee_id: str
    name: str
    email: EmailStr
    department: str


class EmployeeResponse(BaseModel):
    employee_id: str
    name: str
    email: EmailStr
    department: str

    class Config:
        from_attributes = True