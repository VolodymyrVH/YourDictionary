from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

from core.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    color = Column(String(255), nullable=False)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="categories")
    word_categories = relationship("WordCategory", back_populates="category", cascade="all, delete-orphan")


class WordCategory(Base):
    __tablename__ = "word_categories"

    id = Column(Integer, primary_key=True)
    
    word_id = mapped_column(ForeignKey("words.id"), nullable=False)
    category_id  = mapped_column(ForeignKey("categories.id"), nullable=False)

    category = relationship("Category", back_populates="word_categories")   
    word = relationship("Word", back_populates="word_categories")