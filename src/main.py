from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sentry_sdk

from src.app.entrypoints.routers import get_app_router

sentry_sdk.init(
    dsn="https://c5c87c2a4fa341cfd2c9ea1a8a854c9c@o4509422951989248.ingest.de.sentry.io/4509422956445776",
    send_default_pii=True,
)

app = FastAPI()

app.add_middleware(
    middleware_class=CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    # allow_credentials=True,
)

app.include_router(get_app_router())


@app.get("/")
async def welcome():
    return {"Message": "Hello world!"}
