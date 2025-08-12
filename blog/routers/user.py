from fastapi import APIRouter, Depends
from blog import database, schemas
from sqlalchemy.orm import Session
from blog.repository import user
from blog.oauth2 import get_current_user


router = APIRouter(
    tags=['Users']
)
get_db = database.get_db

# write as same
# pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')
@router.post('/user', response_model=schemas.ShowUser)
def create_user(request : schemas.User, db : Session = Depends(get_db)):
    return user.create_new_user(request=request, db=db)


@router.get('/user/details/{user_id}', response_model=schemas.ShowUser)
def user_deatils(user_id: int, db : Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return user.get_user_detail(user_id=user_id, db=db)

