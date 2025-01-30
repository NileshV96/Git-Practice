from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas, database

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return crud.create_user(db, user)

@router.get("/", response_model=list[schemas.UserResponse])
def get_users(db: Session = Depends(database.get_db)):
    return crud.get_users(db)


from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from curd,cshemas,database

router=APIRouter()
@router.post("/",response_model=schemas,UserResponse)
def create_user(user:schemas.UserCreate,db:Session = Depends(database.getdb)):
    return crud.create_user(db,user)

@router.get("/",response_model )