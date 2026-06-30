from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.parts_of_speech import PartOfSpeechCreateSchema, PartOfSpeechResponseSchema, PartOfSpeechUpdateSchema
from models.parts_of_speech import PartOfSpeech
from core.database import get_db


router = APIRouter(prefix="/parts-of-speech", tags=["partofspeech"])


@router.get("/", response_model=list[PartOfSpeechResponseSchema])
def get_all_parts(skip: int = 0, limit = 100, db: Session = Depends(get_db)):
    return (db.query(PartOfSpeech).offset(skip).limit(limit).all())


@router.get("/by-name/{part_name}", response_model=PartOfSpeechResponseSchema)
def get_part(part_name: str, db: Session = Depends(get_db)):
    part_of_speech_db = (db.query(PartOfSpeech).filter(PartOfSpeech.part == part_name).first())
    if not part_of_speech_db:
        raise HTTPException(status_code=404, detail="Part not found")

    return part_of_speech_db


@router.post("/", response_model=PartOfSpeechResponseSchema)
def created_part(part_of_speech: PartOfSpeechCreateSchema, db: Session = Depends(get_db)):
    existing = (db.query(PartOfSpeech).filter(PartOfSpeech.part == part_of_speech.part).first())
    if existing:
        raise HTTPException(status_code=400, detail="Part already exists")

    part_of_speech_db = PartOfSpeech(
        part=part_of_speech.part
    )

    db.add(part_of_speech_db)
    db.commit()
    db.refresh(part_of_speech_db)

    return part_of_speech_db


@router.patch("/{part_of_speech_id}", response_model=PartOfSpeechResponseSchema)
def update_part(part_of_speech_id: int, part_of_speech_update: PartOfSpeechUpdateSchema, db: Session = Depends(get_db)):
    part_of_speech_db = (db.query(PartOfSpeech).filter(PartOfSpeech.id == part_of_speech_id).first())

    if not part_of_speech_db:
        raise HTTPException(status_code=404, detail="Part not found")

    update_data = part_of_speech_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(part_of_speech_db, field, value)

    db.commit()
    db.refresh(part_of_speech_db)

    return part_of_speech_db


@router.delete("/{part_of_speech_id}", status_code=204)
def delete_part(part_of_speech_id: int, db: Session = Depends(get_db)):
    part_of_speech_db = (db.query(PartOfSpeech).filter(PartOfSpeech.id == part_of_speech_id).first())

    if not part_of_speech_db:
        raise HTTPException(status_code=404, detail="Part not found")

    db.delete(part_of_speech_db)
    db.commit()