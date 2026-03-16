from pydantic import BaseModel


class WordCreateSchema(BaseModel):
    word_string: str
    language_id: int
    part_language_id: int
    category_id: int | None = None
    transcription: str | None = None


class WordResponseSchema(BaseModel):
    id: int
    word_string: str
    language_id: int
    part_language_id: int
    category_id: int | None
    transcription: str | None
    user_id: int

    class Config:
        from_attributes = True


class WordUpdateSchema(BaseModel):
    word_string: str | None = None
    language_id: int | None = None
    part_language_id: int | None = None
    category_id: int | None = None
    transcription: str | None = None


class TranslationResponseSchema(BaseModel):
    id: int
    word_id_1: int
    word_id_2: int

    class Config:
        from_attributes = True


class TranslationUpdateSchema(BaseModel):
    word_id_1: int | None = None
    word_id_2: int | None = None


class CategoryCreateSchema(BaseModel):
    name: str
    color: str


class CategoryResponseSchema(BaseModel):
    id: int
    name: str
    color: str
    user_id: int

    class Config:
        from_attributes = True


class CategoryCreateSchema(BaseModel):
    name: str | None = None
    color: str | None = None