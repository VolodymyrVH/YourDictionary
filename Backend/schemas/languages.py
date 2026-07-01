from pydantic import BaseModel, Field, ConfigDict


class LanguageCreateSchema(BaseModel):
    language: str = Field(min_length=1, max_length=50)
    code: str = Field(min_length=2, max_length=3)


class LanguageUpdateSchema(BaseModel):
    language: str | None = Field(None, min_length=1, max_length=50)
    code: str | None = Field(None, min_length=2, max_length=3)


class LanguageResponseSchema(BaseModel):
    id: int
    language: str
    code: str

    model_config = ConfigDict(from_attributes=True)