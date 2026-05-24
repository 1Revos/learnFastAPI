from fastapi import APIRouter, status, HTTPException
from schemas.practical_work_4 import Books

router = APIRouter(
    prefix = "/books",
    tags = ["library2.0"]
)
library_db = []

@router.post("", status_code = status.HTTP_201_CREATED)
async def add_book(new_book: Books):
    if any(new_book.id == book["id"] for book in library_db):
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"Книга с id {new_book.id} уже существует!"
        )
    
    library_db.append(new_book.model_dump())
    return f"Книга с id {new_book.id} добавлена!"

@router.get("/{book_id}", status_code = status.HTTP_200_OK)
async def get_book(book_id: int):
    if not any(book_id == book["id"] for book in library_db):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Книга с id {book_id} отсутствует в библтотеке!",
        )
    
@router.get("", status_code = status.HTTP_200_OK)
async def get_list_books(author: str = None, year: int = None):
    if author == None and year == None:
        return library_db
    
    filtr_list = []
    
    for book in library_db:

        author_nt = (author == None or book["author"] == author)
        year_nt = (year == None or book["year"] == year)

        if author_nt and year_nt:
            filtr_list.append(book)
    
    return filtr_list

@router.put("", status_code = status.HTTP_200_OK)
async def put_book(upd_book: Books):
    if not any(upd_book.id == book["id"] for book in library_db):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Книги с id {upd_book.id} нет!"
        )

    for index, book in enumerate(library_db):

        if upd_book.id == book["id"]:
            library_db[index] = upd_book.model_dump()
    
    return

@router.delete("{book_id}", status_code = status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int):
    if not any(book_id == book["id"] for book in library_db):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Книга с id {book_id} отсутствует в библтотеке!",
        )
    
    for book in enumerate(library_db):

        if book_id == book["id"]:
            library_db.remove(book)
    
    return


    


