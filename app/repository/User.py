from .. import models,schemas,hashing,oauth2
from sqlalchemy.orm import Session
from fastapi import HTTPException,status,Depends

Hash = hashing.Hash


#function to get user email
def get_user_email(db:Session, email):
    user = db.query(models.User).filter(models.User.email == email).first()
    return user


#function to create user
def create(user:schemas.User,db:Session):
    new_user = models.User(name=user.name, email = user.email, password = Hash.bcrypt(user.password))
    existed_user = get_user_email(db,user.email)
    if existed_user:
        raise  HTTPException(status_code=409,detail = 'user already exists')
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#function to get user by id
def get_by_id(id:int,db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The user with the id {id} is not available')
    return user

#function to delete a user 
def destroy(db:Session,current_user=Depends(oauth2.get_current_user)):
    delete_user = db.query(models.User).filter(models.User.id == current_user)#gets the phone with the specific id
    #gets the phone with the specific id and if id is not available
    if not delete_user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the id {id} is not available')
    #if the phone id is available delte the phone
    delete_user.delete(synchronize_session=False)
    db.commit() #commit the datbase to save changes
    return f'The User with the id {current_user} has been deleted'

#function to update a user
#function to update a phone
def update(update_user:schemas.Update_User,db:Session,current_user=Depends(oauth2.get_current_user)): 
    user_for_update = db.query(models.User).filter(models.User.id == current_user)
    if not user_for_update.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Phone with the id {id} is not available')
    
    #incase the user doesn't want to change everything
    if update_user.name == None:
       update_user.name = user_for_update.first().name

    if update_user.email == None:
       update_user.email = user_for_update.first().email

    if update_user.password == None:
       update_user.password = user_for_update.first().password

    #to change the updated password to hash format for security
    if update_user.password != None:
        update_user.password = Hash.bcrypt(update_user.password)

    user_for_update.update(update_user.dict())
    db.commit()
    return {f'User with id {current_user} updated successfully'}

