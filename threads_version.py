import threading
import time
import httpx

from typing import Tuple

Urls = Tuple[str]

urls = ("https://www.google.com", ) * 50

def send_request(url: str, count: int, client: httpx.Client) -> httpx.Response:
    print(f"Sending request #{count}")
    response = client.get(url=url)
    print(f"Received response for #{count} with {response.status_code} status code.")

    return response


def main_threads():
    with httpx.Client() as client:
        tasks = []

        for n, url in enumerate(urls, start=1):
            tasks.append(threading.Thread(target=send_request, args=(url, n, client)))
            tasks[-1].start()

        for task in tasks:
            task.join()


if __name__ == '__main__':
    start = time.perf_counter()
    main_threads()
    end = time.perf_counter()

    threads_duration = end - start
    print(f"Threads duration: {threads_duration}") # Threads duration: 0.26890208304394037
