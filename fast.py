from fastapi import FastAPI


app = FastAPI()

@app.get('/blog/{id}/comments')

def comments(id,limit=10):
    return {'data':{'1','2'}}


@app.get('/blog')

def index(limit=10,published:bool = True):
    if published:
        return {'data':f'{limit} published blogs from the db'}
    else:
        return {'data':f'{limit}  blogs from the db'}
    

@app.get('blog/{id}/comments')
def comments(id,limit=10):
    return {'data':{'1','2'}}    
    

@app.post('/blogs')

def create_blog():
    return {'data':'blog is created'}



