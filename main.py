from fastapi import FastAPI, APIRouter
from routers.hello import router as hello_router
 
app = FastAPI(
    title = "Эдпоинты для FastAPI",
    description = "Изучаем FastAPI",
    version = "0.136.1"
)

app.include_router(hello_router)