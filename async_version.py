import asyncio
import httpx
import time

from typing import Tuple

Urls = Tuple[str]

urls = ("https://www.google.com", ) * 50

async def async_send_request(url: str, count: int, client: httpx.AsyncClient):
    print(f"Sending request for #{count}")
    response = await client.get(url=url)
    print(f"Received response for #{count} with {response.status_code} status code.")

    return response


async def async_main_process(in_urls: Urls = urls):
    async with httpx.AsyncClient() as client:
        async with asyncio.TaskGroup() as group:
            for n, url in enumerate(in_urls, start=1):
                group.create_task(
                    async_send_request(url, n, client)
                )


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(async_main_process(urls))
    end = time.perf_counter()

    duration = end - start

    print(f"Async duration: {duration}")