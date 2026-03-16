from pydantic import BaseModel


class LanguageCreateSchema(BaseModel):
    name: str
    code: str


class LanguageResponseSchema(BaseModel):
    id: int
    name: str
    code: str

    class Config:
        from_attributes = True


class LanguageUpdateSchema(BaseModel):
    name: str | None = None
    code: str | None = None


class PartLanguageCreateSchema(BaseModel):
    part: str


class PartLanguageResponseSchema(BaseModel):
    id: int
    part: str

    class Config:
        from_attributes = True


class PartLanguageUpdateSchema(BaseModel):
    part: str | None = None
