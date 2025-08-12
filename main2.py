from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return { 'data' : 'Blog List' }

# i have written beacause, fastapi goes line by line
# if i have use path /blog/xyz
# then it goes line by line and give error on where i have return path, /blog/id and show error
# because, fastapi check one by one path mathing
# /blog, /xyz
@app.get('/blog/unpublished')
def unpublished():
    return {'data' : 'all unpublished blog'}

@app.get('/blog/{blog_id}')
def index(blog_id:int): # Browser always give input in string, to take input in integer always use data type of input
    return { 'data' : blog_id }


@app.get('/blog/{blog_id}/comments')
def comments(blog_id):
    return { 'data' : {'1', '2'} }