from fastapi import APIRouter, status, HTTPException

router = APIRouter(
    prefix = "",
    tags = ["practical_work_2"]
)

@router.get("/squer/{number}")
async def get_squer(number: int):
    return {"number": number, "square": number ** 2}

@router.get("/greet")
async def get_greet(name: str, age: int):
    return f"Привет, {name}! Тебе {age} лет."

@router.get("/compare")
async def get_compare(a: int, b: int):
    if a > b:
        return {"result": "a больше b"}
    elif a < b:
        return {"result": "b больше a"}
    else:
        return {"Числа равны!"}