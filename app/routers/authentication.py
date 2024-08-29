#login route
from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,database,models,hashing,phone_token
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from datetime import timedelta

Hash = hashing.Hash

router = APIRouter(
    tags=['Authentication']
)

ACCESS_TOKEN_EXPIRE_MINUTES = 10080


@router.post('/login')
def login(user: Annotated[OAuth2PasswordRequestForm, Depends()],db:Session=Depends(database.get_db)):
    user_details = db.query(models.User).filter(models.User.email == user.username).first() #setting the username to email
    user_details_id = user_details.id
    if not user_details:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Invalid Credentials')
    #Verify the user password
    if not Hash.verify(user_details.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Incorrect Password')
    #generate a jwt token and return it
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = phone_token.create_access_token(data={"sub": user.username,"id":user_details_id},expires_delta=access_token_expires)
    return schemas.Token(access_token=access_token, token_type="bearer")
