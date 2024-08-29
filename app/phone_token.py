from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import  InvalidTokenError
from . import schemas
from .config import SECRET_KEY,ALGORITHM


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=10080)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

#verify the jwt token
def verify_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        user_id = payload.get("id")
        if not email:
            raise credentials_exception
        return user_id
    except InvalidTokenError:
        raise credentials_exception
