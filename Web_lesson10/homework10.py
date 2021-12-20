import json
import sys
import httpx
import redis


def get_info_from_api(country) -> dict:
    with httpx.Client() as web_client:
        base_url = "http://universities.hipolabs.com/search?country"

        url = f"{base_url}={country}"

        response = web_client.get(url)
        return response.json()[0]['name']


def get_info_from_cache(country, client):
    val = client.get(country)
    return val


def set_info_to_cache(country, value, client):
    data = client.set(country, value)
    return data


def cash_analyzer(country, client):
    data = get_info_from_cache(country, client)
    if data:
        print(f'{data.decode("utf-8")} - this {country}s university took from cash')
    else:
        data = get_info_from_api(country)
        print(f'{data} - this {country}s university took from api')
        if data:
            state = set_info_to_cache(country=country, value=data, client=client)
            return state


if __name__ == '__main__':
    redis_client = redis.StrictRedis(
    host='redis-12846.c250.eu-central-1-1.ec2.cloud.redislabs.com', # из Endpoint
    port=12846, # из Endpoint
    password='s2xCxXPRTFtywvKC6dHgQHzsNnzj8h9Z' # ваш пароль
)

    cash_analyzer('Ukraine', redis_client)
    cash_analyzer('Bulgaria', redis_client)
    cash_analyzer('Albania', redis_client)
    cash_analyzer('Spain', redis_client)


