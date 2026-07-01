from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from core.database import Base


class Article(Base):
    __tablename__ = "articles"

    id = Column(Integer, primary_key=True)
    article = Column(String(10), nullable=False)
    
    language_id = Column(Integer, ForeignKey("languages.id"), nullable=False)
    gender_id = Column(Integer, ForeignKey("genders.id"), nullable=True)

    language = relationship("Language", back_populates="articles")
    gender = relationship("Gender", back_populates="articles")
    words = relationship("Word", back_populates="article")