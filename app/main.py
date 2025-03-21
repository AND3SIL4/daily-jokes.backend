import os

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

from app.api import jokes

load_dotenv()
app = FastAPI(title="Daily Jokes API REST")

# Constants
VERSION = os.getenv("VERSION")


# Include routers
app.include_router(jokes.router, prefix="/joke", tags=["Jokes"])


@app.get("/")
def root():
    return JSONResponse(
        status_code=200,
        content={
            "app_version": VERSION,
        },
    )
