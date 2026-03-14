from core.database import Session, engine, Base
from models.users import User
from models.words import Word, Translation, Category
from models.languages import Language, PartLanguage

Base.metadata.create_all(engine)

with Session() as session:
    user = User(email="test@mail.com", password="123")
    session.add(user)
    session.commit()