from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class BookBase(BaseModel):
    serial_number: str = Field(..., min_length=6, max_length=6)
    title: str
    author: str
    is_borrowed: bool = False
    borrowed_at: Optional[datetime] = None
    borrower_card_number: Optional[str] = None

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    is_borrowed: bool
    borrower_card_number: Optional[str] = None
    borrowed_at: Optional[datetime] = None

class BookResponse(BookBase):
    id: int

    class Config:
        from_attributes = True