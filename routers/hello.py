from fastapi import APIRouter, status

router = APIRouter(
    prefix = "/about",
    tags = ["Hello"]
)

@router.get("", status_code = status.HTTP_200_OK)
async def get_hello(name: str):
    return {"message": f"Hello, {name}!"}