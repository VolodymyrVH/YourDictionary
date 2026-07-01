from pydantic import BaseModel, Field, ConfigDict


class ArticleCreateSchema(BaseModel):
    article: str = Field(min_length=1, max_length=10)

    language_id: int = Field(gt=0)
    gender_id: int | None = Field(None, gt=0)


class ArticleUpdateSchema(BaseModel):
    article: str | None = Field(None, min_length=1, max_length=10)

    language_id: int | None = Field(None, gt=0)
    gender_id: int | None = Field(None, gt=0)


class ArticleResponseSchema(BaseModel):
    id: int
    article: str

    language_id: int
    gender_id: int

    model_config = ConfigDict(from_attributes=True)