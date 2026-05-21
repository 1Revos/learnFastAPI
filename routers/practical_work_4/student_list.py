from fastapi import APIRouter, status, HTTPException
from schemas.practical_work_4 import Students

router = APIRouter(
    prefix = "/students",
    tags = ["students_list"]
)

students_list = []

@router.get("", status_code = status.HTTP_200_OK)
async def get_students_list():
    return students_list

@router.post("", status_code = status.HTTP_201_CREATED)
def add_student(student: Students):
    students_list.append(student.model_dump())
    return f"Студент {student.name} добавлен."

@router.patch("/{student_id}", status_code = status.HTTP_200_OK)
def patch_avg(student_id: int, new_avg: int):
    if not any(student["id"] == id for student in students_list):
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND,
            detail = f"Студент с id {student_id} не найден."
        )
    
    for student in students_list:
        if student["id"] == student_id:
            student["average_score"] == new_avg
    
    return
    
@router.delete("/{student_id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_student(student_id: int):
    for student in students_list:
        if student["id"] == student_id:
            students_list.remove(student)
    
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = f"Студент с id {student_id} отсутствует."
    )
