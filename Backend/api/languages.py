from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.languages import LanguageCreateSchema, LanguageResponseSchema, LanguageUpdateSchema
from models.languages import Language
from core.database import get_db


router = APIRouter(prefix="/languages", tags=["language"])


@router.get("/", response_model=list[LanguageResponseSchema])
def get_all_languages(skip: int = 0, limit = 100, db: Session = Depends(get_db)):
    return (db.query(Language).offset(skip).limit(limit).all())


@router.get("/by-code/{language_code}", response_model=LanguageResponseSchema)
def get_language(language_code: str,  db: Session = Depends(get_db)):
    language_db = (db.query(Language).filter(Language.code == language_code).first())
    if not language_db:
        raise HTTPException(status_code=404, detail="Language not found")

    return language_db


@router.post("/", response_model=LanguageResponseSchema)
def create_language(language: LanguageCreateSchema, db: Session = Depends(get_db)):
    existing = (db.query(Language).filter(Language.language == language.language, Language.code == language.code).first())
    if existing:
        raise HTTPException(status_code=400, detail="Language already exists")

    language_db = Language(
        language=language.language,
        code=language.code
    )

    db.add(language_db)
    db.commit()
    db.refresh(language_db)

    return language_db


@router.patch("/{language_id}", response_model=LanguageResponseSchema)
def update_language(language_id: int, language_update: LanguageUpdateSchema, db: Session = Depends(get_db)):
    language_db = (db.query(Language).filter(Language.id == language_id).first())

    if not language_db:
        raise HTTPException(status_code=404, detail="Language not found")

    update_data = language_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(language_db, field, value)

    db.commit()
    db.refresh(language_db)

    return language_db


@router.delete("/{language_id}", status_code=204)
def delete_language(language_id: int, db: Session = Depends(get_db)):
    language_db = (db.query(Language).filter(Language.id == language_id).first())

    if not language_db:
        raise HTTPException(status_code=404, detail="Language not found")

    db.delete(language_db)
    db.commit()