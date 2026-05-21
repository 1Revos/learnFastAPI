from fastapi import APIRouter, status, HTTPException
from schemas.practical_work_3 import Movies

router = APIRouter(
    prefix = "/movies",
    tags = ["movies"]
)

movies_db = []

@router.get("", status_code = status.HTTP_200_OK)
async def get_list():
    return movies_db

@router.get("/{movie_id}", status_code = status.HTTP_200_OK)
async def get_movie(movie_id: int):
    if not any(movie["id"] == movie_id for movie in  movies_db):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = "Фильм не найден."
        )
    return (movie for movie in movies_db if movie["id"] == movie_id)

@router.post("", status_code = status.HTTP_201_CREATED)
async def add_movie(movie: Movies):
    movies_db.append(movie.model_dump())
    return {"message": f"Фильм {movie.title} добавлен!"}