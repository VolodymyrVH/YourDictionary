from pydantic import BaseModel, Field, ConfigDict


class GenderCreateSchema(BaseModel):
    gender: str = Field(min_length=1, max_length=50)


class GenderUpdateSchema(BaseModel):
    gender: str | None = Field(None, min_length=1, max_length=50)


class GenderResponseSchema(BaseModel):
    id: int
    gender: str

    model_config = ConfigDict(from_attributes=True)