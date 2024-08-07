from fastapi import FastAPI
from . import models
from .database import engine
from .routers import phone,user,authentication


app = FastAPI()

#register your route in the main.py
app.include_router(phone.router)
app.include_router(user.router)
app.include_router(authentication.router)

#models create the database
models.Base.metadata.create_all(bind=engine)


