from fastapi import APIRouter, Depends, status
from blog import schemas, database
from typing import List
from sqlalchemy.orm import Session
from blog.repository import blog
from blog.oauth2 import get_current_user

router = APIRouter(
    tags=['Blogs'],
    prefix='/blog'
)

get_db = database.get_db

# @router.get('/blog/show', response_model=List[schemas.ShowBlog], tags=['blogs'])
@router.get('/', response_model=List[schemas.ShowBlog])
def all_data(db : Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_all_blog(db)


@router.post('/create', status_code=status.HTTP_201_CREATED)
def create(request : schemas.Blog, db : Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.create_new_blog(request, db)


@router.delete('/delete/{blog_id}', status_code=status.HTTP_204_NO_CONTENT)
def destory(blog_id : int,  db : Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.delete_blog(blog_id=blog_id, db=db)


# update method
@router.put('/update/{blog_id}', status_code=status.HTTP_202_ACCEPTED)
def update_details(blog_id: int, request : schemas.Blog, db : Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.update_blog(blog_id=blog_id, request=request, db=db)


# if successfuly found the details of particular id then status = 200
# else it change
@router.get('/details/{blog_id}', status_code=200, response_model=schemas.ShowBlog)
def details(blog_id:int, db : Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return blog.get_blog_detail(blog_id=blog_id, db=db)