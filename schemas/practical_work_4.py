from pydantic import BaseModel

class Products(BaseModel):
    id: int
    name: str
    price: float
    in_stok: bool

class Students(BaseModel):
    id: int
    name: str
    group: str
    average_score: float

