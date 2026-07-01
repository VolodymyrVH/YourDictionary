from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import relationship

from core.database import Base


class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True)
    word_string = Column(String(255), nullable=False)
    transcription = Column(String(255), nullable=True)
    definition = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now(), onupdate=func.now())

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    language_id = Column(Integer, ForeignKey("languages.id"), nullable=False)
    article_id = Column(Integer, ForeignKey("articles.id"), nullable=True)
    part_of_speech_id = Column(Integer, ForeignKey("parts_of_speech.id"), nullable=True)
    gender_id = Column(Integer, ForeignKey("genders.id"), nullable=True)

    user = relationship("User", back_populates="words")
    language = relationship("Language", back_populates="words")
    article = relationship("Article", back_populates="words")
    gender = relationship("Gender", back_populates="words")
    part_of_speech = relationship("PartOfSpeech", back_populates="words")
    word_categories = relationship("WordCategory", back_populates="word", cascade="all, delete-orphan")