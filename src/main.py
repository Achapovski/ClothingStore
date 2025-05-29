from fastapi import FastAPI

from src.app.entrypoints.routers import get_app_router

app = FastAPI()
app.include_router(get_app_router())


@app.get("/")
async def welcome():
    return {"Message": "Hello world!"}
