from fastapi import FastAPI

app = FastAPI()

@app.get('/')

def abc():

    return {'data':{'name':'BalajiReddyk'}}


@app.get('/about')
def about():

    return {'data':{'Name':'About page'}}


@app.get('bolg/{id}/comments')

def comments(id):

    #fetch comments of blog with id = id

    return {'data':{'1'}}