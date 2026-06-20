from pydantic import BaseModel, Field, ConfigDict


class CategoryCreateSchema(BaseModel):
    name: str = Field(min_length=1)
    color: str = Field(min_length=1, max_length=100)


class CategoryUpdateSchema(BaseModel):
    name: str | None = Field(None, min_length=1)
    color: str | None = Field(None, min_length=1, max_length=100)


class CategoryResponseSchema(BaseModel):
    id: int
    name: str
    color: str
    user_id: int

    model_config = ConfigDict(from_attributes=True)


class WordCategoryCreateSchema(BaseModel):
    word_id: int = Field(gt=0)
    category_id: int = Field(gt=0)


class WordCategoryResponseSchema(BaseModel):
    id: int
    word_id: int
    category_id: int

    model_config = ConfigDict(from_attributes=True) 