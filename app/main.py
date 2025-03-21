import os

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

VERSION = os.getenv("VERSION")


@app.get("/")
def root():
    return JSONResponse(
        status_code=200,
        content={
            "app_version": VERSION,
        },
    )
