from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.users import UserCreateSchema, UserResponseSchema, UserUpdateSchema
from models.users import User
from core.database import get_db
from api.auth import get_current_user, get_password_hash


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", response_model=list[UserResponseSchema])
def get_all(skip: int = 0, limit = 100, db: Session = Depends(get_db)):
    return db.query(User).offset(skip).limit(limit).all()


@router.get("/email/{email}", response_model=UserResponseSchema)
def get_by_email(email: str, db: Session = Depends(get_db)):
    user_db = db.query(User).filter(User.email == email).first()
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    return user_db


#get_current_user_profile
#get_by_id
@router.post("/", response_model=UserResponseSchema)
def create_user(user: UserCreateSchema, db: Session = Depends(get_db)):
    existing = db.query(User).filter((User.email == user.email)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    user_db = User(**user.model_dump(exclude={"password"}),
                   hashed_password = get_password_hash(user.hashed_password),)

    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    return user_db


#update_user
#delete_user