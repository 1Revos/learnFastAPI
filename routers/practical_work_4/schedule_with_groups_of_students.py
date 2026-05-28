from fastapi import APIRouter, status, HTTPException
from schemas.schedule_with_groups_of_students import Lessons

router = APIRouter(
    prefix = "/lessons",
    tags = ["schedule_with_groups_of_students"]
)

lessons_db = []

@router.post("", status_code = status.HTTP_201_CREATED)
async def add_lessons(new_lessons: Lessons):
    if any(lessons["id"] == new_lessons.id for lessons in lessons_db):
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = f"Урок с id {new_lessons.id} уже существует!"
        )
    
    lessons_db.append(new_lessons.model_dump())

    return f"Урок с id {new_lessons.id} успешно добавлен!"

@router.get("", status_code = status.HTTP_200_OK)
async def get_list():
    return lessons_db

@router.get("/{lessons_id}", status_code = status.HTTP_200_OK)
def get_lessons(lessons_id: int):
    if not any(lessons["id"] == lessons_id for lessons in lessons_db):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Урок с id {lessons_id} отсутствует!"
        )
        
    for lessons in lessons_db:

        if lessons["id"] == lessons_id:
            return lessons
        
@router.put("/{lessons_id}", status_code = status.HTTP_200_OK)
def put_lessons(lessons_id: int, new_lessons: Lessons):
    if not any(lessons["id"] == lessons_id for lessons in lessons_db):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Урок с id {lessons_id} отсутствует!"
        )
    
    for index, lessons in enumerate(lessons_db):

        if lessons_id == lessons["id"]:
            lessons_db[index] = new_lessons.model_dump()
        return lessons_db[index]

@router.delete("/{lessons_id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_lessons(lessons_id: int):
    if not any(lessons["id"] == lessons_id for lessons in lessons_db):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Урок с id {lessons_id} отсутствует!"
        )
    
    for lessons in lessons_db:

        if lessons_id == lessons["id"]:
            lessons_db.remove(lessons)
    return 

@router.post("/{lessons_id}/students", status_code = status.HTTP_201_CREATED)
def add_student(lessons_id: int, name_student: str):
    lessons = next((lesson for lesson in lessons_db if lesson["id"] == lessons_id), None)
    if lessons is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Урок с id {lessons_id} не найден."
        )
    
    if name_student in lessons["students"]:
          raise HTTPException(
            status_code = status.HTTP_409_CONFLICT,
            detail = f"Студент '{name_student}' уже находится на уроке с id {lessons_id}."
        )
    
    lessons["students"].append(name_student)

    return f"Студент {name_student} успешно добавлен!"

@router.delete("/{lessons_id}/students/{name}", status_code = status.HTTP_204_NO_CONTENT)
def delete_student(lessons_id: int, name: str):
    lessons = next((lesson for lesson in lessons_db if lesson["id"] == lessons_id), None)
    if lessons is None:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Урок с id {lessons_id} отсутствует!"
        )
    if name not in lessons["students"]:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Студент '{name}' не найден на уроке с id {lessons_id}."
        )
    
    
    lessons["students"].remove(name)
    
    return