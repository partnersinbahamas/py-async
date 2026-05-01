import time

import httpx
import multiprocessing
from typing import Tuple

Urls = Tuple[str]

urls = ("https://www.google.com", ) * 50

def send_request(count: int, url: str):
    print(f"Sending request #{count}")
    response = httpx.get(url=url)
    print(f"Received response for #{count} with {response.status_code} status code.")

    return response

def main_process(in_urls: Urls = urls):
    tasks = []

    for n, url in enumerate(in_urls,start=1):
        tasks.append(multiprocessing.Process(target=send_request, args=(n, url)))
        tasks[-1].start()

    for task in tasks:
        task.join()


if __name__ == '__main__':
    start = time.perf_counter()
    main_process(urls)
    end = time.perf_counter()

    duration = end - start

    print(f"Multiprocessing duration: {duration}") # Multiprocessing duration: 1.1814555829623714