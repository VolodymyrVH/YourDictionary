from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.categories import CategoryCreateSchema, CategoryResponseSchema, CategoryUpdateSchema, WordCategoryCreateSchema, WordCategoryResponseSchema
from models.categories import Category, WordCategory
from models.users import User
from core.database import get_db
from api.auth import get_current_user


router = APIRouter(prefix="/category", tags=["category"])


@router.get("/", response_model=list[CategoryResponseSchema])
def get_user_categories(skip: int = 0, limit = 100, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    user_db = db.query(User).filter(User.id == current_user.id).first()
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    return (db.query(Category).filter(Category.user_id == current_user.id).offset(skip).limit(limit).all())


@router.get("/category", response_model=CategoryResponseSchema)
def get_user_category_name(category_name: str, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    category_db = (db.query(Category).filter(Category.user_id == current_user.id, Category.name == category_name).first())
    if not category_db:
        raise HTTPException(status_code=404, detail="Category not found")

    return category_db


@router.post("/", response_model=CategoryResponseSchema)
def create_category(category: CategoryCreateSchema, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    existing = (db.query(Category).filter(Category.name == category.name, Category.user_id == current_user.id).first())
    if existing:
        raise HTTPException(status_code=400, detail="Category already exists")

    category_db = Category(
        name=category.name,
        color=category.color,
        user_id=current_user.id
    )

    db.add(category_db)
    db.commit()
    db.refresh(category_db)

    return category_db


@router.patch("/{category_id}", response_model=CategoryResponseSchema)
def update_category(category_id: int, category_update: CategoryUpdateSchema, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    category_db = (db.query(Category).filter(Category.id == category_id, Category.user_id == current_user.id).first())

    if not category_db:
        raise HTTPException(status_code=404, detail="Category not found")

    update_data = category_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(category_db, field, value)

    db.commit()
    db.refresh(category_db)

    return category_db


@router.delete("/{category_id}", status_code=204)
def delete_category(category_id: int, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    category_db = (db.query(Category).filter(Category.id == category_id, Category.user_id == current_user.id).first())

    if not category_db:
        raise HTTPException(status_code=404, detail="Category not found")

    db.delete(category_db)
    db.commit()


#def get_word_category
#def create_word_category
#def delete_word_category