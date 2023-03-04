import asyncio
import time


async def async_sleep(n):
    print("Before Sleep .... ", n)
    await asyncio.sleep(n)
    print("After Sleep .... ", n)


async def print_hello():
    print("Hello!!")


async def main():
    start_time = time.time()
    try:
        await asyncio.gather(asyncio.wait_for(async_sleep(30), 5), async_sleep(7), print_hello())
    except asyncio.TimeoutError:
        print("Encountered timeout error!!")
    # end
    print("Total time: ", time.time() - start_time)


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