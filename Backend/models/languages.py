from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from core.database import Base


class Language(Base):
    __tablename__ = "language"

    id = Column(Integer, primary_key=True)
    language = Column(String(50), nullable=False)
    code = Column(String(3), nullable=False)

    words = relationship("Word", back_populates="language")