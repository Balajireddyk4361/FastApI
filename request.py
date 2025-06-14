# from fastapi import FastAPI

# from pydantic import Basemodal

# app=FastAPI()

# class blogs(Basemodal):
#     pass


# @app.post('/blog')
# def create_blog(request:blogs):
#     return {'data ':'blog is created'}

from fastapi import FastAPI

from typing import Optional

from pydantic import BaseModel

app_fast=FastAPI()

class Blog(BaseModel):
    title:str
    body:str
    published:Optional [bool]


@app_fast.post('/blog')

def create_blog(request:Blog):
    return request
    return {'data': 'Blog is created'}


@app_fast.post('/blogs')
 def create_blog(blog:Blog):
   return {'data':f'Blog is created with title as{blog.title}'}
   
  