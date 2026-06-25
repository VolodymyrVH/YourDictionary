from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, func
from sqlalchemy.orm import mapped_column, relationship

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
    language_id = Column(Integer, nullable=True) #add after creating tables
    article_id = Column(Integer, nullable=True) #add after creating tables
    parts_of_speach_id = Column(Integer, nullable=True) #add after creating tables
    gender_id = Column(Integer, nullable=True) #add after creating tables

    user = relationship("User", back_populates="words")
    word_categories = relationship("WordCategory", back_populates="word", cascade="all, delete-orphan")