from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.categories import WordCategoryCreateSchema, WordCategoryResponseSchema
from schemas.words import WordResponseSchema
from models.categories import Category, WordCategory
from models.users import User
from models.words import Word
from core.database import get_db
from api.auth import get_current_user


router = APIRouter(prefix="/word-category", tags=["word-category"])


@router.get("/{category_id}", response_model=list[WordResponseSchema])
def get_word_category(category_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)): #Add word after table Word
    word_category_db = (db.query(Category).filter(Category.id == category_id, Category.user_id == current_user.id).first())

    if not word_category_db:
        raise HTTPException(status_code=404, detail="Category not found")
    
    words = (db.query(Word).join(WordCategory).filter(WordCategory.category_id == category_id, Word.user_id == current_user.id).all())

    return words


@router.post("/", response_model=WordCategoryResponseSchema)
def create_word_category(word_category: WordCategoryCreateSchema, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    existing = (db.query(WordCategory).filter(WordCategory.word_id == word_category.word_id, WordCategory.category_id == word_category.category_id).first())
    if existing:
        raise HTTPException(status_code=400, detail="Releationshps already exists")

    category = (db.query(Category).filter(Category.id == word_category.category_id, Category.user_id == current_user.id).first())
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    word = (db.query(Word).filter(Word.id == word_category.word_id, Word.user_id == current_user.id).first())
    if not word:
        raise HTTPException(status_code=404, detail="Word not found")

    word_category_db = WordCategory(
        word_id=word_category.word_id,
        category_id=word_category.category_id,
    )

    db.add(word_category_db)
    db.commit()
    db.refresh(word_category_db)

    return word_category_db


@router.delete("/{word_category_id}", status_code=204)
def delete_word_category(word_category_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    word_category_db = (db.query(WordCategory).join(Category).filter(WordCategory.id == word_category_id, Category.user_id == current_user.id).first())

    if not word_category_db:
        raise HTTPException(status_code=404, detail="Releationships not found")

    db.delete(word_category_db)
    db.commit()