from fastapi import FastAPI
from . import models
from .database import engine
from .routers import phone,user,authentication
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # List allowed origins
    allow_credentials=True,
    allow_methods=["*"],  # List allowed methods or use ["*"] for all methods
    allow_headers=["*"],  # List allowed headers or use ["*"] for all headers
)

#register your route in the main.py
app.include_router(phone.router)
app.include_router(user.router)
app.include_router(authentication.router)

#models create the database
models.Base.metadata.create_all(bind=engine)


