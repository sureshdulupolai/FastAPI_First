from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# we will not use this beacuse query parameter doesnt change the path
# that why we directly declare in function
# @app.get('/blog?limit=10&published=true')
# Opton -> http://localhost:8000/blog?hi=1
@app.get('/blog')
def index(limit = 10, published:bool = True, sort: Optional[str] = None):
    # only get 10 published blogs
    if published:
        return { 'data' : f'Blog List of {limit}' }
    else:
        return {'data' : '5 Blog List'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data' : 'all unpublished blog'}

@app.get('/blog/{blog_id}')
def blog_details(blog_id:int):
    return { 'data' : blog_id }


# FastAPI is very smart that hey find out with is path parameter and query parameter
@app.get('/blog/{blog_id}/comments')
def comments(blog_id, limit=10):
    return { 'data' : {'1', '2'} }