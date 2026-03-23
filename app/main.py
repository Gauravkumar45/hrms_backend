from fastapi import FastAPI
from app.db.database import Base, engine
from app.routes import employee, attendance
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="HRMS Lite API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal Server Error. Please try again later."}
    )

@app.get("/")
def root():
    return {"message": "HRMS Lite API Running. Access /docs for API documentation."}

@app.get("/health")
def health_check():
    return {"status": "healthy. HRMS Lite API is up and running."}

app.include_router(employee.router)
app.include_router(attendance.router)
