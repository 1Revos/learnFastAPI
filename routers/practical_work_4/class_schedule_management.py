from fastapi import APIRouter, status, HTTPException
from schemas.practical_work_4 import Lessons

router = APIRouter(
    prefix = "/lessons",
    tags = ["class schedule management"]
)

lessons_db = []

@router.post("", status_code = status.HTTP_201_CREATED)
async def add_lessons(new_lessons: Lessons):
    if any(new_lessons.id == lessons["id"] for lessons in lessons_db):
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"Урок с id {new_lessons.id} уже существует!"
        )
    
    lessons_db.append(new_lessons.model_dump())

    return f"Урок с id {new_lessons.id} успешно создан!"

@router.get("", status_code = status.HTTP_200_OK)
async def get_list():
    return lessons_db

@router.patch("/{lessons_id}", status_code = status.HTTP_200_OK)
async def patch_lessons(lessons_id: int, new_time: int = None, new_day: int = None):
    if not any(lessons["id"] == lessons_id for lessons in lessons_db):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Урок с id {lessons_id} не найден."
        )
    
    for lessons in lessons_db:

        if lessons["id"] == lessons_id:

            if not new_time and not new_day:
                return lessons_db
            
            if new_time and new_day:
                lessons["new_time"] = new_time
                lessons["new_tday"] = new_day

                return lessons_db

            if new_time:
                lessons["new_time"] = new_time

                return lessons_db
            
            if new_day:
                lessons["new_tday"] = new_day

                return lessons_db
            

@router.delete("/{lessons_id}", status_code = status.HTTP_204_NO_CONTENT)
async def delete_lessons(lessons_id: int):
    if not any(lessons["id"] == lessons_id for lessons in lessons_db):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Урок с id {lessons_id} не найден."
        )
    
    for lessons in lessons_db:

        if lessons["id"] == lessons_id:

            lessons_db.remove(lessons)

    return 


