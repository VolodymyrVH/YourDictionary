from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from contextlib import asynccontextmanager

from core.database import init_db

from models.users import *
from models.categories import *
from models.words import *
from models.genders import *
from models.parts_of_speech import *
from models.articles import *
from models.languages import *
from models.translations import *

from api import users, auth, categories, word_categories, words, genders, parts_of_speech, languages, articles

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(categories.router)
app.include_router(word_categories.router)
app.include_router(words.router)
app.include_router(genders.router)
app.include_router(parts_of_speech.router)
app.include_router(languages.router)
app.include_router(articles.router)


@app.get("/")
def read_root():
    return {"stauts": "ok"}