from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.core.database import Base

class Language(Base):
    __tablename__ = "languages"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    code: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)

    words: Mapped[list["Word"]] = relationship(back_populates="language")

    def __repr__(self):
        return f"Language(id={self.id!r}, name={self.name!r}, code={self.code!r})"


class PartLanguage(Base):
    __tablename__ = "parts_language"

    id: Mapped[int] = mapped_column(primary_key=True)
    part: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)

    words: Mapped[list["Word"]] = relationship(back_populates="part_language")

    def __repr__(self):
        return f"PartLanguage(id={self.id!r}, part={self.part!r})"