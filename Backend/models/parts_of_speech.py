from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from core.database import Base


class PartOfSpeech(Base):
    __tablename__ = "parts_of_speech"

    id = Column(Integer, primary_key=True)
    part = Column(String(50), nullable=False)

    words = relationship("Word", back_populates="part_of_speech")