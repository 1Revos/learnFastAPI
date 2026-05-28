from pydantic import BaseModel

class Lessons(BaseModel):
   id: int
   subject: str
   teacher: str
   day: str
   time: str
   students: list[str] 