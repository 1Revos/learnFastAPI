from fastapi import APIRouter, status, HTTPException
from schemas.practical_work_4 import Products

router = APIRouter(
    prefix = "/products",
    tags = ["menage_products"]
)

product_db = []

@router.post("", status_code = status.HTTP_201_CREATED)
async def add_product(product: Products):
    product_db.append(product.model_dump())
    return {"message": f"Товар {product.name} добавлен!"}

@router.get("", status_code = status.HTTP_200_OK)
async def get_list_products():
    return product_db

@router.put("/{id}", status_code = status.HTTP_200_OK)
async def put_product(id: int, new_product: Products):

    for index, product in enumerate(product_db):
        if product.id == id:
            product_db[index] = new_product.model_dump()
            return {"message": "Данные обновлены!"}

    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = f"Продукта с id: {id} не существует!"
    )

@router.delete("/{id}", status_code = status.HTTP_204_NO_CONTENT)
async def delete_product(id: int):

    for product in product_db:
        if product["id"] == id:
            product_db.remove(product)
            return 
        
    raise HTTPException(
        status_code = status.HTTP_404_NOT_FOUND,
        detail = "Продукт с id:{id} не найден!"
    )
    
     