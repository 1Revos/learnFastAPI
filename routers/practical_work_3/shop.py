from fastapi import APIRouter, status, HTTPException
from schemas.practical_work_3 import Products

router = APIRouter(
    prefix = "/products",
    tags = ["shop"]
)

shop_db = []

@router.post("", status_code = status.HTTP_201_CREATED)
async def add_product(product: Products):
    shop_db.append(product.model_dump())
    return {"message": f"Продукт {product.name} добавлен."}

@router.get("", status_code = status.HTTP_200_OK)
async def get_list_product(min_price: int  = None, max_price: int = None):

    if min_price is None and max_price is None:
        return shop_db
    
    new_list = []
    for product in shop_db:
        price = product["price"]

        min_price_xd = (min_price is None or min_price >= price)
        max_price_xd = (max_price is None or max_price <= price)
        
        if max_price_xd and min_price_xd:
            new_list.append(product)
    
    return new_list


    
