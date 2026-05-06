from fastapi import APIRouter, status

router = APIRouter(
    prefix = "/about",
    tags = ["practical_work_1"]
)

@router.get("", status_code = status.HTTP_200_OK)
async def get_hello(name: str):
    return {"message": f"Hello, {name}!"}