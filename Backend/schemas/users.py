from datetime import datetime
from pydantic import BaseModel, Field, EmailStr, ConfigDict

class UserCreateSchema(BaseModel):
    email: EmailStr = Field(min_length=1, max_length=100)
    password: str = Field(min_length=8) #_hash


class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8) #_hash


class UserUpdateSchema(BaseModel):
    email: EmailStr | None = Field(None, min_length=1, max_length=100)
    password: str | None = Field(None, min_length=8) #_hash


class UserResponseSchema(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)