from fastapi import APIRouter, status, HTTPException
from schemas.practical_work_3 import Books

router = APIRouter(
    prefix = "/books",
    tags = ["library"]
)

library_db = []

@router.get("", status_code = status.HTTP_200_OK)
async def get_list():
    return library_db

@router.get("/{books_id}", status_code = status.HTTP_200_OK)
async def get_book(books_id: int):
    if books_id not in library_db:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Такой книги нет."
        )
    return (book for book in library_db if book["id"] == books_id)

@router.get("/author", status_code = status.HTTP_200_OK)
async def get_autor_books(author: str):
    if author not in library_db:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND
        )
    
    return (book for book in library_db if book["author"] == author)

@router.post("/add", status_code = status.HTTP_201_CREATED)
async def add_book(book: Books):
    library_db.append(book.model_dump())
    return {"message": f"Книга {book.title} добавлен!"}