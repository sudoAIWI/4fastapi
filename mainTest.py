from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()



@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    #return published
    if published:
        return {'data': f'{limit} published blog from the db'}
    else:
        return{'data': f'{limit} blogs from the db'}


@app.get('/')
def index():
    return {'data': {'bloglist'}}

@app.get('/about')
def about():
    return {'data':{'about page'}}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data': id}

@app.get('/blog/{id}/comments')
def comments(id):
    return {'data': {'1', '2'}}


class Blog(BaseModel):
    title: str
    body:str
    published: Optional[bool]

@app.post('/blog')
def create_blog(request: Blog):
    return request
    return{'data': f'Blog is created with title as {request.title}'}
