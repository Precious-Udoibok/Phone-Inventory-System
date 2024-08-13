#phone routes
from fastapi import APIRouter,Depends,status
from typing import  List
from .. import schemas,database,oauth2
from sqlalchemy.orm import Session
from ..repository import phone

router = APIRouter(
    prefix='/phone',
    tags=['phone'],
    dependencies=[Depends(oauth2.get_current_user)],
    )

#view all phones with out the id
@router.get('/',response_model=List[schemas.ShowPhone]) 
#pass in the database instance
def get_phones(db:Session= Depends(database.get_db)):
    return phone.get_all(db)


#Add a new phone to the database Create a new item
@router.post('/',status_code=status.HTTP_201_CREATED)
#create an instance for the database
def create(user_phone:schemas.Phone, db:Session=Depends(database.get_db)):
    return phone.create(user_phone,db)


#view a phone by id with the id
@router.get('/{id}',response_model=schemas.ShowPhone)
def get_by_id(id:int,db:Session=Depends(database.get_db)):
    return phone.get_by_id(id,db)

#delete a phone
@router.delete('/{id}',status_code=status.HTTP_202_ACCEPTED)
def destroy(id,db:Session=Depends(database.get_db)):
    return phone.destroy(id,db)


#update a phone
@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,user_phone:schemas.Update_Phone,db:Session=Depends(database.get_db)):
    return phone.update(id,user_phone,db)
