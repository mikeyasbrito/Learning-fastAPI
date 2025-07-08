from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import MainSchema

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=MainSchema)
def reed_root():
    return {'message': 'Olá Mundo!'}


@app.get('/html', response_class=HTMLResponse)
def read_html():
    return """
    <html>
        <head>
            <title>FastAPI Zero</title>
        </head>
        <body>
            <h1>Olá Mundo!</h1>
        </body>
    </html>
    """
