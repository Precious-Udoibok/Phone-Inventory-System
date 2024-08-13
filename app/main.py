from fastapi import FastAPI
from . import models
from .database import engine
from .routers import phone,user,authentication
from starlette.middleware.cors import CORSMiddleware


app = FastAPI(
    title="A Phone Inventory System api",
    description='''
            This is a phone inventory api that includes endpoints for phones(add,delete, update and view) phones\n
            endpoints for users(add,edit,delete and view) users, including authentication for all endpoints except signup
''',
    version="1.0.0"
)

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


