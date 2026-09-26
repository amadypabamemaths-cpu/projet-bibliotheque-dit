from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    role: str

class UserResponse(UserCreate):
    id: int
    class Config:
        from_attributes = True

class BookCreate(BaseModel):
    title: str
    author: str
    isbn: str

class BookResponse(BookCreate):
    id: int
    available: bool
    class Config:
        from_attributes = True

class BorrowCreate(BaseModel):
    user_id: int
    book_id: int
    borrow_date: str