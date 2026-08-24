from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class WordCreateSchema(BaseModel):
    word_string: str = Field(min_length=1)
    language_id: int = Field(gt=0)
    article_id: int | None = Field(None, gt=0)
    part_of_speech_id: int | None = Field(None, gt=0)
    transcription: str | None = Field(None, min_length=1)
    gender_id: int | None = Field(None, gt=0)
    definition: str | None = Field(None, min_length=1)


class WordUpdateSchema(BaseModel):
    word_string: str | None = Field(None, min_length=1)
    language_id: int | None = Field(None, gt=0)
    article_id: int | None = Field(None, gt=0)
    part_of_speech_id: int | None = Field(None, gt=0)
    transcription: str | None = Field(None, min_length=1)
    gender_id: int | None = Field(None, gt=0)
    definition: str | None = Field(None, min_length=1)

    
class WordResponseSchema(BaseModel):
    id: int
    user_id: int
    word_string: str
    language_id: int
    article_id: int | None
    part_of_speech_id: int
    transcription: str
    gender_id: int | None
    definition: str
    created_at: datetime
    updated_at: datetime | None

    model_config = ConfigDict(from_attributes=True)


class WordNameResponseSchema(BaseModel):
    id: int
    user_id: int
    word_string: str
    language: str
    article: str | None
    part_of_speech: str
    transcription: str
    gender: str | None
    definition: str
        
    model_config = ConfigDict(from_attributes=True)
        