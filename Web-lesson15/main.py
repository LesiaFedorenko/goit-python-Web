from fastapi import FastAPI
import aiohttp
# import asyncio
from bs4 import BeautifulSoup
from pydantic import BaseModel

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///./database.db")
Session = sessionmaker(bind=engine)


class Film(BaseModel):
    cinema: str
    title: str
    age: str
    session: str


app = FastAPI()

def get_db():
    return Session()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get('/film_multiplex/{film_id}', response_model=Film)
async def get_film_multiplex():
    async with aiohttp.ClientSession() as session:
        url = "https://multiplex.ua/ru/cinema/kyiv/lavina"
        async with session.get(url) as response:
            text = await response.read()
            results = BeautifulSoup(text, "lxml").findAll('div', class_="film")
            for result in results:
                return Film(cinema="Multiplex",
                            title=result.find('div', class_="title").text.replace('\n', '').lstrip(),
                            age=result.find('span', class_="age").text,
                            session=result.find('div', class_="sessions").text.replace('\n', ' ').lstrip().rstrip(),
                            )


@app.get('/film_oskar/{film_id}', response_model=Film)
async def get_film_oskar():
    async with aiohttp.ClientSession() as session:
        url = "https://oskar.kyiv.ua/smart/sessions?date_select=2022-01-14&slider=0,24"
        async with session.get(url) as response:
            text = await response.read()
            results = BeautifulSoup(text, "lxml").findAll('div', class_="filter-result__item")
            for result in results:
                return Film(cinema="Oskar",
                            title=result.find('div', class_="name").text,
                            age=result.find('span', class_="gallery__visual_age").text,
                            session=result.find('div', class_="filter-result__time-wrap").text.replace('\n',
                                                                                                       ' ').lstrip().rstrip(),
                            )
