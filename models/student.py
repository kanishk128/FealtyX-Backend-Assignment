from pydantic import BaseModel

class StudentCreate(BaseModel):
    ID: int
    Name: str
    Age: int
    Email: str
        