import asyncio

async def async_sleep():
    print("Before Sleep ....")
    await asyncio.sleep(5)
    print("After Sleep ....")

async def print_hello():
    print("Hello!!")


async def main():
    # await keyword: Awaits the response of the corresponding async_sleep co-routine

    """
    So what happens with the await call is the wait call is not blocking. It allows execution of other code routines.
    However, it does stop the execution of going further down in this function i.e. print_hello() will not be executed
    until async_sleep() finishes.

    But because we only have one main coroutine routine running, and inside of these, we call two more code routines.
    These are all still being executed sequentially.

    --> Basically we are running sequentially
    """
    await async_sleep()
    await print_hello()

if __name__=="__main__":
    asyncio.run(main())







"""
import asyncio
import time
import requests
import aiohttp


async def get_url_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    urls = ['https://google.com',
            'https://wikipedia.org/wiki/Concurrency',
            'https://python.org',
            'https://pypi.org/project/requests/',
            'https://docs.python.org/3/library/asyncio-task.html',
            'https://www.apple.com/',
            'https://medium.com']

    start = time.time()
    sync_text_response = []
    for url in urls:
        sync_text_response.append(requests.get(url).text)

    end_time = time.time()
    print('Requests time:', end_time - start)

    start = time.time()
    tasks = []
    for url in urls:
        tasks.append(asyncio.create_task(get_url_response(url)))

    async_text_response = await asyncio.gather(*tasks)

    end_time = time.time()
    print('Async requests time:', end_time - start)


if __name__ == '__main__':
    asyncio.run(main())
"""