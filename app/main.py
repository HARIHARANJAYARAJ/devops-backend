from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List

from . import models, schemas, crud
from .database import engine, get_db


# Creates tables if they do not exist.
# Alembic handles changes to existing tables.
models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="Student Management API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://3.110.171.142",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Student Management API is running"}


@app.get("/students", response_model=List[schemas.StudentOut])
def read_students(db: Session = Depends(get_db)):
    return crud.get_students(db)


@app.get("/students/{student_id}", response_model=schemas.StudentOut)
def read_student(student_id: int, db: Session = Depends(get_db)):
    student = crud.get_student(db, student_id)

    if not student:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return student


@app.post(
    "/students",
    response_model=schemas.StudentOut,
    status_code=201,
)
def create_student(
    student: schemas.StudentCreate,
    db: Session = Depends(get_db),
):
    try:
        return crud.create_student(db, student)

    except IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=400,
            detail="A student with this roll number or email already exists",
        )


@app.put(
    "/students/{student_id}",
    response_model=schemas.StudentOut,
)
def update_student(
    student_id: int,
    student: schemas.StudentUpdate,
    db: Session = Depends(get_db),
):
    updated = crud.update_student(
        db,
        student_id,
        student,
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return updated


@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db),
):
    deleted = crud.delete_student(
        db,
        student_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Student not found",
        )

    return {
        "message": "Student deleted successfully"
    }