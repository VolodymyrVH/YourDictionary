from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.words import WordCreateSchema, WordResponseSchema, WordUpdateSchema
from models.words import Word
from models.users import User
from core.database import get_db
from api.auth import get_current_user


router = APIRouter(prefix="/words", tags=["word"])


@router.get("/", response_model=list[WordResponseSchema])
def get_all_words(skip: int = 0, limit = 100, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return (db.query(Word).filter(Word.user_id == current_user.id).offset(skip).limit(limit).all())


@router.get("/by-name/{word}", response_model=WordResponseSchema)
def get_word(word: str, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    word_db = (db.query(Word).filter(Word.user_id == current_user.id, Word.word_string == word).first())
    if not word_db:
        raise HTTPException(status_code=404, detail="Word not found")

    return word_db


@router.post("/word", response_model=WordResponseSchema)
def create_word(word: WordCreateSchema, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    word_db = Word(
        user_id=current_user.id,
        word_string=word.word_string,
        language_id=word.language_id,
        article_id=word.article_id,
        part_of_speach_id=word.part_of_speach_id,
        transcription=word.transcription,
        gender_id=word.gender_id,
        definition=word.definition
    )

    db.add(word_db)
    db.commit()
    db.refresh(word_db)

    return word_db


@router.patch("/{word_id}", response_model=WordResponseSchema)
def update_word(word_id: int, word_update: WordUpdateSchema, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    word_db = (db.query(Word).filter(Word.id == word_id, Word.user_id == current_user.id).first())

    if not word_db:
        raise HTTPException(status_code=404, detail="Word not found")

    update_data = word_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(word_db, field, value)

    db.commit()
    db.refresh(word_db)

    return word_db


@router.delete("/{word_id}", status_code=204)
def delete_word(word_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    word_db = (db.query(Word).filter(Word.id == word_id, Word.user_id == current_user.id).first())

    if not word_db:
        raise HTTPException(status_code=404, detail="Word not found")

    db.delete(word_db)
    db.commit()
