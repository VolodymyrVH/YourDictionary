from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.users import UserCreateSchema, UserResponseSchema, UserUpdateSchema
from models.users import User
from core.database import get_db


router = APIRouter(prefix="/users", tags=["users"])


#Temporarily
@router.get("/", response_model=list[UserResponseSchema])
def get_all(skip: int = 0, limit = 100, db: Session = Depends(get_db)):
    return db.query(User).offset(skip).limit(limit).all()
#get_by_email
#get_current_user_profile
#get_by_id
@router.post("/", response_model=UserResponseSchema)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    existing = db.query(User).filter((User.email == user.email)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user_db = User(**user.model_dump())

    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db


#update_user
#delete_user