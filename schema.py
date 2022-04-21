from pydantic import BaseModel, EmailStr
from typing import Optional

class userInput(BaseModel):
    
    email : EmailStr
    first_name : str
    last_name : str
    password : str

    class Config:
        orm_mode = True



