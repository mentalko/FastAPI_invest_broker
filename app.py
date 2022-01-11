from fastapi.applications import FastAPI
from fastapi_pagination import add_pagination
from src.api import router

app = FastAPI()
app.include_router(router)

add_pagination(app)