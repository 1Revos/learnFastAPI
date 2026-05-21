from fastapi import APIRouter, status, HTTPException
from schemas.practical_work_3 import Books

router = APIRouter(
    prefix = "/books",
    tags = ["library"]
)

library_db = []

# @router.get("", status_code = status.HTTP_200_OK)
# async def get_list():
#     return library_db

@router.get("/{book_id}", status_code = status.HTTP_200_OK)
async def get_book(book_id: int):
    if not any(book["id"] == book_id for book in library_db):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Книга с id {book_id} не найдена"
        )
    return (book for book in library_db if book["id"] == book_id)

@router.get("", status_code = status.HTTP_200_OK)
async def get_autor_books(author: str = None):
    if author is None:
        return library_db
    
    return (book for book in library_db if book["author"] == author)

@router.post("/add", status_code = status.HTTP_201_CREATED)
async def add_book(book: Books):
    library_db.append(book.model_dump())
    return {"message": f"Книга {book.title} добавлен!"}