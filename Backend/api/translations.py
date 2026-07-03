from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.translations import TranslationCreateSchema, TranslationResponseSchema
from models.translations import Translation
from models.words import Word
from models.users import User
from core.database import get_db
from api.auth import get_current_user


router = APIRouter(prefix="/translations", tags=["translation"])


@router.get("/by-word/{translation_word}", response_model=TranslationResponseSchema)
def get_translation_word(translation: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    translation_db = (db.query(Translation).join(Word, Translation.word_id == Word.id).filter(Translation.word_id == translation, Word.user_id == current_user).first())
    if not translation_db:
        raise HTTPException(status_code=404, detail="Translation pair not found")

    return translation_db


@router.post("/", response_model=TranslationCreateSchema)
def create_translation(translations: TranslationCreateSchema, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    existing = (db.query(Translation).filter(Translation.word_id == translations.word_id, Translation.translated_word_id == translations.translated_word_id, Word.user_id == current_user).first())
    if existing:
        raise HTTPException(status_code=400, detail="Translation pait already exists")

    translation_db = Translation(
        word_id=translations.word_id,
        translated_word_id=translations.translated_word_id
    )

    db.add(translation_db)
    db.commit()
    db.refresh(translation_db)

    return translation_db


@router.delete("/{translation_id}", status_code=204)
def delete_translation(translation_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    translation_db = (db.query(Translation).filter(Translation.id == translation_id, Word.user_id == current_user).first())

    if not translation_db:
        raise HTTPException(status_code=404, detail="Translation pair not found")

    db.delete(translation_db)
    db.commit()