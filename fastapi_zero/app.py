from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def reed_root():
    return {'message': 'Olá Mundo!'}
