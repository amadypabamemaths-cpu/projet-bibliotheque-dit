from fastapi import FastAPI, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
import models, schemas
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Bibliothèque DIT")

# --- LIVRES ---
@app.post("/books/", response_model=schemas.BookResponse)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@app.get("/books/", response_model=List[schemas.BookResponse])
def get_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

# --- UTILISATEURS ---
@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/", response_model=List[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

# --- EMPRUNTS ---
@app.post("/borrows/")
def borrow_book(borrow: schemas.BorrowCreate, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == borrow.book_id).first()
    if not book or not book.available:
        raise HTTPException(status_code=400, detail="Livre indisponible")
    
    book.available = False
    new_borrow = models.Borrow(**borrow.model_dump())
    db.add(new_borrow)
    db.commit()
    return {"message": "Emprunt enregistré avec succès"}