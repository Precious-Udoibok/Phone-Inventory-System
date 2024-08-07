from sqlalchemy.orm import Session
from .. import models,schemas
from fastapi import HTTPException,status


#operations or functions for the routers

#function to view all the phones in the database
def get_all(db:Session):
    phones = db.query(models.Phone).all()
    return phones

#function to get phone by id
def get_by_id(id,db:Session):
    phone = db.query(models.Phone).filter(models.Phone.id == id).first()
    #if phone is not available raise an Http exception
    if not phone:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'The phone with the id {id} is not available')
    #if phone is avaialble
    return phone


#functions to create a new phone
def create(user_phone:schemas.Phone,db:Session):
    #create a new phone using the sqlalchamey model
    new_phone = models.Phone(name=user_phone.name, brand=user_phone.brand, color=user_phone.color, 
                             price=user_phone.price,quantity=user_phone.quantity, description= user_phone.description)
    db.add(new_phone)
    db.commit() #commit is so that it will work
    db.refresh(new_phone)
    return {f'The phone {user_phone.name} has been created successfully'}


#function to delete a phone by id
def destroy(id:int,db:Session):
    phone = db.query(models.Phone).filter(models.Phone.id == id)#gets the phone with the specific id
    #gets the phone with the specific id and if id is not available
    if not phone.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Phone with the id {id} is not available')
    #if the phone id is available delte the phone
    phone.delete(synchronize_session=False)
    db.commit() #commit the datbase to save changes
    return f'Phone with the id {id} has been deleted '


#function to update a phone
def update(id:int,user_phone:schemas.Update_Phone,db:Session):
    phone = db.query(models.Phone).filter(models.Phone.id == id)
    if not phone.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Phone with the id {id} is not available')
    
    #incase the user doesn't want to change everything
    #if the user doesn't give any update, set it to the default
    if user_phone.name == None:
       user_phone.name = phone.first().name

    if user_phone.brand == None:
       user_phone.brand = phone.first().brand

    if user_phone.color == None:
       user_phone.color = phone.first().color

    if user_phone.price == None:
       user_phone.price = phone.first().price

    if user_phone.quantity == None:
       user_phone.quantity = phone.first().quantity

    if user_phone.description == None:
       user_phone.description = phone.first().description

    phone.update(user_phone.dict())
    db.commit()
    return {f'Phone with id {id} updated successfully'}