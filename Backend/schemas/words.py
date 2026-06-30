from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict

#change after adding new tables
class WordCreateSchema(BaseModel):
    word_string: str = Field(min_length=1)
    language_id: int | None = Field(None, gt=0)
    article_id: int | None = Field(None, gt=0)
    parts_of_speech_id: int | None = Field(None, gt=0)
    transcription: str | None = Field(None, min_length=1)
    gender_id: int | None = Field(None, gt=0)
    definition: str | None = Field(None, min_length=1)


class WordUpdateSchema(BaseModel):
    word_string: str | None = Field(None, min_length=1)
    language_id: int | None = Field(None, gt=0)
    article_id: int | None = Field(None, gt=0)
    parts_of_speech_id: int | None = Field(None, gt=0)
    transcription: str | None = Field(None, min_length=1)
    gender_id: int | None = Field(None, gt=0)
    definition: str | None = Field(None, min_length=1)

    
class WordResponseSchema(BaseModel):
    id: int
    user_id: int
    word_string: str
    language_id: int
    article_id: int
    parts_of_speech_id: int
    transcription: str
    gender_id: int
    definition: str
    created_at: datetime
    updated_at: datetime | None

    model_config = ConfigDict(from_attributes=True)
    