from pydantic import BaseModel, Field, ConfigDict


class PartOfSpeechCreateSchema(BaseModel):
    part: str = Field(min_length=1, max_length=50)


class PartOfSpeechUpdateSchema(BaseModel):
    part: str | None = Field(None, min_length=1, max_length=50)


class PartOfSpeechResponseSchema(BaseModel):
    id: int
    part: str

    model_config = ConfigDict(from_attributes=True)