from fastapi import FastAPI
from blog import model
from .database import engine
# from passlib.context import CryptContext
from .routers import blog, user, authentication

app = FastAPI()

model.Base.metadata.create_all(engine)

app.include_router(authentication.auth_router)
app.include_router(blog.router)
app.include_router(user.router)






# Use Pydantic
# While posting the status code is by default = 200 is good but actual code of post request is 201
# @app.post('/blog', status_code=201) -> this is the not dynamic every time we need to define
# Auto Comple By FastAPI, For status code also

# @app.post('/blog/create', status_code=status.HTTP_201_CREATED, tags=['blogs'])
# def create(request : schemas.Blog, db : Session = Depends(get_db)):
#     new_blog = model.Blog(title=request.title, body=request.body, user_id=1)
#     db.add(new_blog)
#     db.commit() # run
#     db.refresh(new_blog)
#     return new_blog


# @app.get('/blog/show', response_model=List[schemas.ShowBlog], tags=['blogs'])
# def all_data(db : Session = Depends(get_db)):
#     blogs = db.query(model.Blog).all()
#     return blogs



# ----------------------------------------------------------------------------------
# this is direct not good in fastapi
# @app.post('/blog')
# def create(title, body):
#     return {'title' : title, 'body' : body}

