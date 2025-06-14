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



@app_id.get('/string')

def string(limit):
    return {'data':f'{limit} blogs from db'}


@app_id.get('/bala')

def add():
     return {'data':1}





@app_id.get('/Balaji')

def index(limit,published):
    return published

    if published:
        return {'data':f'{limit} published blogs from the db'}
    else:
        return {'data':f'{limit}  blogs from the db'}
    
    # out put
  # http://localhost:8000/Balaji?limit=10&published=true  


@app_id.get('/Balajireddy')

def login(limit=10,published:bool=False):


    if published:
                return {'data':f'{limit} published blogs from the db'}
    else:
        return {'data':f'{limit}  blogs from the db'}
    



#----------------------------------------------

