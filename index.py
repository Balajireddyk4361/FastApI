from fastapi import FastAPI

app_id=FastAPI()

@app_id.get('/')


def add():
    return {'data':{'name':'Royal reddy'}}


# @app_id.get('/about')
# def about():
#     return {'table':{'id':10000}}

@app_id.get('/blog/{id}')

def show(id :int):
    return {'data':id}

@app_id.get('/blog/{id}/comments')

def comments(id : int):
    return {'data':{1,2}}


