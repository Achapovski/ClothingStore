from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def welcome():
    return {"Message": "Hello"}
