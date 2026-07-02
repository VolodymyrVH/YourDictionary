from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas.articles import ArticleCreateSchema, ArticleResponseSchema, ArticleUpdateSchema
from models.articles import Article
from core.database import get_db


router = APIRouter(prefix="/articles", tags=["article"])


@router.get("/", response_model=list[ArticleResponseSchema])
def get_all_articles(skip: int = 0, limit = 100, db: Session = Depends(get_db)):
    return (db.query(Article).offset(skip).limit(limit).all())


@router.get("/by-name/{article_name}", response_model=ArticleResponseSchema)
def get_article(article_name: str,  db: Session = Depends(get_db)):
    article_db = (db.query(Article).filter(Article.article == article_name).first())
    if not article_db:
        raise HTTPException(status_code=404, detail="Article not found")

    return article_db


@router.post("/", response_model=ArticleResponseSchema)
def create_article(article: ArticleCreateSchema, db: Session = Depends(get_db)):
    existing = (db.query(Article).filter(Article.article == article.article).first())
    if existing:
        raise HTTPException(status_code=400, detail="Article already exists")

    article_db = Article(
        article=article.article,
        language_id=article.language_id,
        gender_id=article.gender_id
    )

    db.add(article_db)
    db.commit()
    db.refresh(article_db)

    return article_db


@router.patch("/{article_id}", response_model=ArticleResponseSchema)
def update_article(article_id: int, article_update: ArticleUpdateSchema, db: Session = Depends(get_db)):
    article_db = (db.query(Article).filter(Article.id == article_id).first())

    if not article_db:
        raise HTTPException(status_code=404, detail="Article not found")

    update_data = article_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(article_db, field, value)

    db.commit()
    db.refresh(article_db)

    return article_db


@router.delete("/{article_id}", status_code=204)
def delete_article(article_id: int, db: Session = Depends(get_db)):
    article_db = (db.query(Article).filter(Article.id == article_id).first())

    if not article_db:
        raise HTTPException(status_code=404, detail="Article not found")

    db.delete(article_db)
    db.commit()