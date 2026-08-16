from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.words import WordCreateSchema, WordResponseSchema, WordUpdateSchema
from schemas.categories import CategoryResponseSchema
from schemas.translations import TranslationResponseSchema
from models.words import Word
from models.users import User
from models.translations import Translation
from models.categories import WordCategory, Category
from core.database import get_db
from api.auth import get_current_user


router = APIRouter(prefix="/words", tags=["word"])


@router.get("/", response_model=list[WordResponseSchema])
def get_all_words(skip: int = 0, limit = 100, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return (db.query(Word).filter(Word.user_id == current_user.id).offset(skip).limit(limit).all())


@router.get("/by-name/{word}", response_model=WordResponseSchema)
def get_word(word: str, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    word_db = (db.query(Word).filter(Word.word_string == word, Word.user_id == current_user.id).first())
    if not word_db:
        raise HTTPException(status_code=404, detail="Word not found")

    return word_db


@router.get("/{word_id}/categories", response_model=list[CategoryResponseSchema])
def get_word_categories(word_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    categorie_db = db.query(Category).join(WordCategory).filter(WordCategory.word_id == word_id, Category.user_id == current_user.id).all()
    if not categorie_db:
        raise HTTPException(status_code=404, detail="Word not found")

    return categorie_db


@router.get("/{word_id}/translations", response_model=list[WordResponseSchema])
def get_word_transaltion(word_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    translation_db = (db.query(Word).join(Translation, Translation.translated_word_id == Word.id).filter(Translation.word_id == word_id, Word.user_id == current_user.id).all())
    if not translation_db:
        raise HTTPException(status_code=404, detail="Word not found")

    return translation_db


@router.get("/filtered_words", response_model=list[WordResponseSchema])
def get_filtered_words(skip: int = 0, 
                       limit = 100,
                       language_id: int | None = None,
                       part_of_speech_id: int | None = None,
                       gender_id: int | None = None, 
                       current_user: User = Depends(get_current_user), 
                       db: Session = Depends(get_db)):
    query = db.query(Word).filter(Word.user_id == current_user.id)

    if language_id:
        query = query.filter(Word.language_id == language_id)
    if part_of_speech_id:
        query = query.filter(Word.part_of_speech_id == part_of_speech_id)
    if gender_id:
        query = query.filter(Word.gender_id == gender_id)
    
    return (query.order_by(Word.id).offset(skip).limit(limit).all())


@router.post("/word", response_model=WordResponseSchema)
def create_word(word: WordCreateSchema, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    word_db = Word(
        user_id=current_user.id,
        word_string=word.word_string,
        language_id=word.language_id,
        article_id=word.article_id,
        part_of_speech_id=word.part_of_speech_id,
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
