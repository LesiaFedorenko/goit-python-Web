import aiohttp
import asyncio
from bs4 import BeautifulSoup
from datetime import date, timedelta
import sqlite3


def insert_multiple_records(records):
    try:
        sqlite_connection = sqlite3.connect('sqlite_python.db')
        cursor = sqlite_connection.cursor()

        cursor.execute("create table lang (url, info)")
        sqlite_insert_query = """INSERT INTO sqlitedb_info
                                 (url, info)
                                 VALUES (?, ?);"""


        cursor.executemany(sqlite_insert_query, records)
        sqlite_connection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print(error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()


async def func1():
    async with aiohttp.ClientSession() as session:
        url = "https://www.meteoprog.ua/ua/weather/Kyiv/tomorrow/"
        async with session.get(url) as response:
            text = await response.read()
            result = BeautifulSoup(text, "lxml").find('div', class_="today-temperature").text.replace(' ', '').replace(
                '\n', '').replace('C', '')
            insert_multiple_records(result)
            print(result)
            return result


async def func2():
    async with aiohttp.ClientSession() as session:
        url = "https://meteo.ua/34/kiev/tomorrow"
        async with session.get(url) as response:
            text = await response.read()
            result = BeautifulSoup(text, "lxml").find('div', class_="weather-detail__main-degree").text.replace(' ', '')
            insert_multiple_records(result)
            print(result)
            return result


async def func3():
    async with aiohttp.ClientSession() as session:
        url = "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BA%D0%B8%D0%B5%D0%B2/"
        today = date.today()
        tomorrow = today + timedelta(days=1)
        url_new = url + str(tomorrow)
        async with session.get(url_new) as response:
            text = await response.read()
            result = BeautifulSoup(text, "lxml").find('div', class_="main loaded").find('div', class_="max").text[6:]
            insert_multiple_records(result)
            print(result)
            return result


async def main():
    sites_soup = asyncio.gather(func1(), func2(), func3())
    await sites_soup


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()
