from sqlalchemy import String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database import Base


class Word(Base):
    __tablename__ = "words"

    id: Mapped[int] = mapped_column(primary_key=True)
    word_string: Mapped[str] = mapped_column(nullable=False)
    language_id: Mapped[int] = mapped_column(ForeignKey("languages.id"), nullable=False)
    part_language_id: Mapped[int] = mapped_column(ForeignKey("parts_language.id"), nullable=False)
    category_id: Mapped[int | None] = mapped_column(ForeignKey("categories.id"), nullable=True)
    transcription: Mapped[str] = mapped_column(String(100), nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    __table_args__ = (
        UniqueConstraint("word_string", "language_id"),
    )

    user: Mapped["User"] = relationship(back_populates="words")
    language: Mapped["Language"] = relationship(back_populates="words")
    part_language: Mapped["PartLanguage"] = relationship(back_populates="words")
    category: Mapped["Category"] = relationship(back_populates="words")

    def __repr__(self):
        return f"Word(id={self.id!r}, word_string={self.word_string!r}, language_id={self.language_id!r})"


class Translation(Base):
    __tablename__ = "translations"

    id: Mapped[int] = mapped_column(primary_key=True)
    word_id_1: Mapped[int] = mapped_column(ForeignKey("words.id"), nullable=False)
    word_id_2: Mapped[int] = mapped_column(ForeignKey("words.id"), nullable=False)

    __table_args__ = (
        UniqueConstraint("word_id_1", "word_id_2"),
    )

    def __repr__(self):
        return f"Translation(id={self.id!r}, word1={self.word_id_1!r}, word2={self.word_id_2!r})"


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    color: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="categories")
    words: Mapped[list["Word"]] = relationship(back_populates="category")

    def __repr__(self):
        return f"Category(id={self.id!r}, name={self.name!r}, user_id={self.user_id!r})"
