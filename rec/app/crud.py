from sqlalchemy.orm import Session
from . import models, schemas
from datetime import datetime

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.dict())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def get_books(db: Session):
    return db.query(models.Book).all()

def delete_book(db: Session, book_id: int):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book

def update_book_status(db: Session, book_id: int, book_update: schemas.BookUpdate):
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if db_book:
        db_book.is_borrowed = book_update.is_borrowed
        db_book.borrowed_at = book_update.borrowed_at if book_update.is_borrowed else None
        db_book.borrower_card_number = book_update.borrower_card_number if book_update.is_borrowed else None
        db.commit()
        db.refresh(db_book)
    return db_book