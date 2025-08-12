# pydantic => is also know as schemas
from pydantic import BaseModel
from typing import List

class BlogBase(BaseModel):
    title : str
    body : str

class Blog(BlogBase):
    class Config():
        orm_mode = True
        

class User(BaseModel):
    name : str
    email : str
    password : str


class ShowUser(User):

    name : str
    email : str
    blogs : List[Blog] = []

    class Config():
        orm_mode = True

# Inherit class created for blog, and show same data which class column have in Blog
# {'id' : 1}, doesnt give id because we have not assign in Blog basemodel
class ShowBlog(Blog):
    
    creator : ShowUser
    # This line update, Blog Basemodel, and show only {'title'}, nothing else
    # title : str
    class Config():
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None