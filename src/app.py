from fastapi.applications import FastAPI
from fastapi_pagination import add_pagination
from . import api 

app = FastAPI()
app.include_router(api.router)

add_pagination(app)