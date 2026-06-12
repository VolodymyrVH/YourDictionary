from sqlalchemy import Column, Integer, String, Date, TIMESTAMP, CheckConstraint, UniqueConstraint, func

from core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())