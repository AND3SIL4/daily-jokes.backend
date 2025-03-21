import os

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.api import jokes

load_dotenv()
app = FastAPI(title="Daily Jokes API REST")
# Allow cors
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Constants
VERSION = os.getenv("VERSION")


# Include routers
app.include_router(jokes.router, prefix="/joke", tags=["Jokes"])


@app.get("/")
def root():
    return JSONResponse(
        status_code=200,
        content={"app_version": VERSION, "developed_by": "Felipe Silva (and3sil4)"},
    )
