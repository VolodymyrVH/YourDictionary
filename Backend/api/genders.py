from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.genders import GenderCreateSchema, GenderResponseSchema, GenderUpdateSchema
from models.genders import Gender
from core.database import get_db


router = APIRouter(prefix="/genders", tags=["gender"])


@router.get("/", response_model=list[GenderResponseSchema])
def get_all_genders(skip: int = 0, limit = 100, db: Session = Depends(get_db)):
    return (db.query(Gender).offset(skip).limit(limit).all())


@router.get("/by-name/{gender_name}", response_model=GenderResponseSchema)
def get_gender(gender_name: str,  db: Session = Depends(get_db)):
    gender_db = (db.query(Gender).filter(Gender.gender == gender_name).first())
    if not gender_db:
        raise HTTPException(status_code=404, detail="Gender not found")

    return gender_db


@router.post("/", response_model=GenderResponseSchema)
def created_gender(gender: GenderCreateSchema, db: Session = Depends(get_db)):
    existing = (db.query(Gender).filter(Gender.gender == gender.gender).first())
    if existing:
        raise HTTPException(status_code=400, detail="Gender already exists")

    gender_db = Gender(
        gender=gender.gender
    )

    db.add(gender_db)
    db.commit()
    db.refresh(gender_db)

    return gender_db


@router.patch("/{gender_id}", response_model=GenderResponseSchema)
def update_gender(gender_id: int, gender_update: GenderUpdateSchema, db: Session = Depends(get_db)):
    gender_db = (db.query(Gender).filter(Gender.id == gender_id).first())

    if not gender_db:
        raise HTTPException(status_code=404, detail="Gender not found")

    update_data = gender_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(gender_db, field, value)

    db.commit()
    db.refresh(gender_db)

    return gender_db


@router.delete("/{gender_id}", status_code=204)
def delete_gender(gender_id: int, db: Session = Depends(get_db)):
    gender_db = (db.query(Gender).filter(Gender.id == gender_id).first())

    if not gender_db:
        raise HTTPException(status_code=404, detail="Gender not found")

    db.delete(gender_db)
    db.commit()