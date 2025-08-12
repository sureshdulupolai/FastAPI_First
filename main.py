# uvicorn main:app --reload
# main -> file name, app -> instance

from fastapi import FastAPI

# Creating a instance of this app
app = FastAPI()

# call as -> path, routes, endpoints
@app.get('/') # also know as decorator
def index(): # path operation function
    # return 'Heyy'
    return { 'data' : {'name' : 'suresh'} }

@app.get('/about')
def about():
    return {'data' : 'about page'}