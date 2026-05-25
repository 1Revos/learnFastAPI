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

class Books(BaseModel):
    id: int
    title: str
    author: str
    year: int
    available: str

class Posts(BaseModel):
    id: int
    title: str
    content: str
    author: str

class Lessons(BaseModel):
    id: int
    subject: str
    teacher: str
    day: str
    time: str
