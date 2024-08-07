# Route behind authentication
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from . import phone_token

#login route will give you your JWT token
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return phone_token.verify_token(token,credentials_exception)
