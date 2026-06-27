from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from core.database import Base


class Gender(Base):
    __tablename__ = "genders"

    id = Column(Integer, primary_key=True)
    gender = Column(String(50), nullable=False)

    words = relationship("Word", back_populates="genders")