import asyncio
import time
import requests # does not support async
import aiohttp # supports async


async def get_url_response(url):
    # 3 control stages: 2 async code line and 1 await and at each line it can give control back to main event loop
    # to continue with the further execution
    # which is not possible with sync_text_response.append(requests.get(url).text) in line 29 as the
    # requests.get(url).text is a blocking event for the main event loop
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
