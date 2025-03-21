from pydantic import BaseModel
from typing import Optional


class JokeBase(BaseModel):
    content: str


class JokeCreate(JokeBase):
    pass


class JokeResponse(JokeBase):
    id: int
    score: Optional[float] = None

    class Config:
        orm_model = True


class JokeRating(BaseModel):
    score: int
