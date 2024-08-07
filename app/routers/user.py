#routers for users
from fastapi import APIRouter,status,Depends
from .. import database,schemas,hashing,oauth2
from sqlalchemy.orm import Session
from ..repository import User

get_db = database.get_db
Hash = hashing.Hash

router = APIRouter(
    prefix='/user', #prefix for the user route
    tags=['user'] #differentiate the user route and phone route
)


# endpoint for user signup
#create a user
@router.post('/',status_code=status.HTTP_201_CREATED,response_model=schemas.Show_User)
def signup(user:schemas.User, db:Session=Depends(get_db)):
    return User.create(user,db)


#endpoint to get user by id without displaying id and password
@router.post('/{id}',response_model=schemas.Show_User)
def get_user(id:int,db:Session=Depends(get_db),current_user=Depends(oauth2.get_current_user)):
    return User.get_by_id(id,db)

#endpoint to delete a user
#delete your account
@router.delete('/{id}',status_code=status.HTTP_202_ACCEPTED)
def destroy(id,db:Session=Depends(database.get_db),current_user=Depends(oauth2.get_current_user)):
    return User.destroy(id,db)

#endpoint to update a user details
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,user_phone:schemas.Update_User,db:Session=Depends(database.get_db),current_user=Depends(oauth2.get_current_user)):
    return User.update(id,user_phone,db)
