from fastapi import FastAPI

app = FastAPI()

@app.get('/')

def index():

    return {'data':{'name':'BalajiReddyk'}}


@app.get('/about')
def about():

    return {'data':{'Name':'About page'}}