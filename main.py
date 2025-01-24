from typing import List

from fastapi import Depends, FastAPI, HTTPException
from pydantic.v1.utils import GetterDict

import database
import schemas
import models
from database import db_state_default

app = FastAPI()

@app.get("/movies/", response_model=List[schemas.Movie])
def get_movies():
    return list(models.Movie.select())
    # movies = crud.get_movies()
    # return movies

@app.post("/movies/", response_model=schemas.Movie)
def add_movie(movie: schemas.MovieBase):
    movie = models.Movie.create(**movie.dict())
    return movie

@app.get("/movies/{movie_id}", response_model=schemas.Movie)
def get_movie(movie_id: int):
    db_movie = models.Movie.filter(models.Movie.id == movie_id).first()
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@app.delete("/movies/{movie_id}", response_model=schemas.Movie)
def delete_movie(movie_id: int):
    db_movie = models.Movie.filter(models.Movie.id == movie_id).first()
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    db_movie.delete_instance()
    return db_movie


@app.get("/actors/", response_model=List[schemas.Actor])
def get_actors():
    return list(models.Actor.select())
    # movies = crud.get_movies()
    # return movies

@app.get("/actors/{actor_id}", response_model=schemas.Actor)
def get_movie(actor_id: int):
    db_movie = models.Actor.filter(models.Actor.id == actor_id).first()
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie


@app.post("/actors/", response_model=schemas.Actor)
def add_movie(movie: schemas.ActorCreate):
    movie = models.Actor.create(**movie.dict())
    return movie


@app.delete("/actors/{actor_id}", response_model=schemas.Actor)
def delete_actor(actor_id: int):
    db_movie = models.Actor.filter(models.Actor.id == actor_id).first()
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    db_movie.delete_instance()
    return db_movie


@app.post("/movies/{movie_id}/actors", response_model=schemas.Movie)
def post_movieactors(movie_id: int):
    db_movie = models.Movie.filter(models.Movie.id == movie_id).first()
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie
























#śmieci
"""
@app.post("/actors/", response_model=schemas.Actor)
def add_actor(movie: schemas.ActorBase):
    movie = models.Actor.create(**movie.dict())
    return movie

@app.get("/actors/{actor_id}", response_model=List[schemas.Actor])
def get_actors():
    return list(models.Actor.select())
    # movies = crud.get_movies()
    # return movies

@app.post("/actors/{actor_id}", response_model=schemas.Movie)
def add_actor(movie: schemas.ActorBase):
    movie = models.Actor.create(**movie.dict())
    return movie

    """