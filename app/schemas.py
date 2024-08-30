from pydantic import BaseModel,EmailStr
from typing import Optional

class Phone(BaseModel):
    name:str
    brand:str
    color:str
    price:str
    quantity:int
    description:str

#to show the phone without the id
class ShowPhone(Phone):
    class Config():
        orm = True #set it to this, because we are using the orm query

class ShowPhone_ID(BaseModel):
    id:int
    name:str
    brand:str
    color:str
    price:str
    quantity:int
    description:str

#Class or schema to update the phone
class Update_Phone(BaseModel):
    name:Optional[str] = None
    brand:Optional[str] = None
    color:Optional[str] = None
    price:Optional[str] = None
    quantity:Optional[int] = None
    description:Optional[str] = None

#schema for signup
class User(BaseModel):
    name:str
    email:EmailStr
    password:str

#schema to update the user
class Update_User(BaseModel):
    name:Optional[str] = None
    email:Optional[EmailStr] = None
    password:Optional[str] = None


#create a schema or class to show user with password and id
class Show_User(BaseModel):
    name:str
    email:EmailStr

    class Config():
        orm = True #set it to this, because we are using the orm query

#schema for authentication
class login(BaseModel):
    email:str
    password:str


#schema for the token
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
