from pydantic import BaseModel

class Feedback(BaseModel):
    name: str
    text: str

class Numbers(BaseModel):
    a: int
    b: int

class Movies(BaseModel):
    id: int
    title: str
    year: int
    rating: float

class Books(BaseModel):
    id: int
    title: str
    author: str
    year: int

class Products(BaseModel):
    id: int
    name: str
    price: float