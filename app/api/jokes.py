from datetime import datetime

from fastapi import APIRouter, HTTPException, Depends
from app.schemas.joke import JokeCreate, JokeResponse, JokeRating
from app.db import models, session


router = APIRouter()


@router.get("/daily")
def get_joke_daily():
    today = datetime.today().strftime(format="%Y-%m-%d")
    db = session.get_db()

    joke = db.get_joke_by_date(today)

    if not joke:
        joke = "Hoy no se encontró ningún chiste :("
        raise HTTPException(status_code=400, detail="No se encontró ningún chiste :(")
    return joke


@router.post("/", response_model=dict)
def add_joke(joke: JokeCreate):
    db = session.get_db()
    db.add_joke(joke)
    return {"message": "Chiste añadido correctamente"}


@router.post("/{joke_id}/rate", response_model=dict)
def rate_joke(joke_id: int, rating: JokeRating):
    db = session.get_db()
    result = db.rate_joke(joke_id=joke_id, score=rating.score)
    if not result:
        raise HTTPException(status_code=404, detail="Chiste no encontrado")
    return {"message": "Chiste calificado correctamente"}
