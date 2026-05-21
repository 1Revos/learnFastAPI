from fastapi import APIRouter, status, HTTPException
from schemas.practical_work_3 import Feedback, Numbers

router = APIRouter(
    prefix = "",
    tags = ["practical_work_3"]
)

feedback_bd = []


@router.post("/feedback", status_code = status.HTTP_201_CREATED)
async def create_feedback(feedback: Feedback):
    feedback_bd.append(feedback.model_dump())
    return {"message": "Спасибо за отзыв, Иван!"}

@router.post("/calc", status_code = status.HTTP_200_OK)
def calculate(numbers: Numbers):
    if numbers.b == 0:
        raise HTTPException(
            status_code = status.HTTP_400_BAD_REQUEST,
            detail = "Деление на ноль невозможно"
        )
    return {
        "sum": numbers.a + numbers.b, 
        "sub": numbers.a - numbers.b, 
        "mul": numbers.a * numbers.b, 
        "div": numbers.a / numbers.b
        }


