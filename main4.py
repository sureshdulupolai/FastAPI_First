from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# @app.post('/blog')
# def createBlog():
#     return {'data' : 'blog is created' }


class Blog(BaseModel):
    title : str
    body: str
    published_at: Optional[bool]


@app.post('/blog')
def createBlog(request: Blog):
    return {'data' : f'blog is created with title {request.title}' }


# Start with "python file.py"
# if __name__ == "__main__":
#     uvicorn.run(app, host='127.0.0.1', port=9000)