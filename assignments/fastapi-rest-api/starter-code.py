from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str

books: List[Book] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

@app.get("/items", response_model=List[Book])
def get_items():
    return books

@app.post("/items", response_model=Book)
def create_item(book: Book):
    books.append(book)
    return book

@app.get("/items/{item_id}", response_model=Book)
def get_item(item_id: int):
    for book in books:
        if book.id == item_id:
            return book
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Book)
def update_item(item_id: int, updated_book: Book):
    for idx, book in enumerate(books):
        if book.id == item_id:
            books[idx] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for idx, book in enumerate(books):
        if book.id == item_id:
            del books[idx]
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
