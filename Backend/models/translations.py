from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from core.database import Base


class Translation(Base):
    __tablename__ = "translations"

    id = Column(Integer, primary_key=True)
    word_id = Column(Integer, ForeignKey("words.id"), nullable=False)
    translated_word_id = Column(Integer, ForeignKey("words.id"), nullable=False)

    word_origin = relationship("Word", foreign_keys=[word_id], back_populates="translations_from")
    word_translated = relationship("Word", foreign_keys=[translated_word_id], back_populates="translations_to")