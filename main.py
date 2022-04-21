from http.client import HTTPException
from ssl import SSLSession
from typing import Optional
from fastapi import Depends, status, HTTPException, Request
from fastapi import FastAPI
import schema
from sqlalchemy.orm import Session

app = FastAPI()

import postgres_db

postgres_db.Base.metadata.create_all(bind = postgres_db.engine)


@app.post('/register/', status_code=status.HTTP_201_CREATED, response_model=schema.userInput)
def create_user(user: schema.userInput, db : Session = Depends(postgres_db.get_db)):
    user_dict = user.dict()
    new_user = postgres_db.User(**user_dict)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return (new_user)
