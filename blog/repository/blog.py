from sqlalchemy.orm import Session
from blog import model
from blog import schemas
from fastapi import HTTPException, status

def get_all_blog(db: Session):
    blogs = db.query(model.Blog).all()
    return blogs


def create_new_blog(request: schemas.Blog, db: Session):
    new_blog = model.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit() # run
    db.refresh(new_blog)
    return new_blog


def delete_blog(blog_id: int, db: Session):
    blog = db.query(model.Blog).filter(model.Blog.id == blog_id)

    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {blog_id} not found")

    blog.delete(synchronize_session=False)
    db.commit()
    return {'data' : f'destory details for id {blog_id}'}


def update_blog(blog_id: int, request: schemas.Blog, db: Session):
    blog = db.query(model.Blog).filter(model.Blog.id == blog_id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f'Blog with id {blog_id} not found!')
    
    # request = full object passing to update, 
    blog.update(request.dict())  # ✅ Convert to dictionary
    db.commit()  # ✅ Commit changes to DB
    return { 'updated' : f'updated successfully for id : {blog_id}' }


def get_blog_detail(blog_id:int, db: Session):
    blogs = db.query(model.Blog).filter(model.Blog.id == blog_id).first()
    if not blogs:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return { 'details' : f'Blog with the id {blog_id} is not available'}

        # Do this Both in One Line
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog with the id {blog_id} is not available')
    return blogs