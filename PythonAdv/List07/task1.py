import asyncio
import aiohttp

from prywatne import API_KEY 

async def fetch_cat_facts(session):
    async with session.get("https://cat-fact.herokuapp.com/facts/random") as response:
        return await response.json()

async def fetch_postman_collections(session):
    headers = {"X-eBirdApiToken": API_KEY}
    async with session.get("https://api.ebird.org/v2/data/obs/KZ/recent", headers=headers) as response:
        return await response.json()

async def get():
    async with aiohttp.ClientSession() as session:
        cat_facts_task = asyncio.create_task(fetch_cat_facts(session))
        postman_collections_task = asyncio.create_task(fetch_postman_collections(session))

        cat_facts = await cat_facts_task
        postman_collections = await postman_collections_task

        print("Cat Fact:", cat_facts['text'])
        print("Postman Collection:", postman_collections[1])

asyncio.run(get())