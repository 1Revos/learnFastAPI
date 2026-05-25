from fastapi import FastAPI, APIRouter
from routers.practical_work_1 import router as pw1_router
from routers.practical_work_2 import router as pw2_router
from routers.practical_work_3.exercise_1 import router as pw3_router
from routers.practical_work_3.movies import router as movies_router
from routers.practical_work_3.library import router as library_router
from routers.practical_work_3.shop import router as shop_router
from routers.practical_work_4.menage_products import router as products_router
from routers.practical_work_4.library import router as library2_router
from routers.practical_work_4.mini_blog import router as mini_blog
from routers.practical_work_4.class_schedule_management import router as class_schedule_management_router

app = FastAPI(
    title = "Эдпоинты для FastAPI",
    description = "Изучаем FastAPI",
    version = "0.136.1"
)

app.include_router(pw1_router)
app.include_router(pw2_router)
app.include_router(pw3_router)
app.include_router(movies_router)
app.include_router(library_router)
app.include_router(shop_router)
app.include_router(products_router)
app.include_router(library2_router)
app.include_router(mini_blog)
app.include_router(class_schedule_management_router)