from pydantic import BaseModel, Field, ConfigDict


class TranslationCreateSchema(BaseModel):
    word_id: int = Field(gt=0)
    translated_word_id: int = Field(gt=0)


class TranslationResponseSchema(BaseModel):
    id: int
    word_id: int
    translated_word_id: int

    model_config = ConfigDict(from_attributes=True)