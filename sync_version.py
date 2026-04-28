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


def main_sync():
    with httpx.Client() as client:
        for n, url in enumerate(urls, start=1):
            send_request(url, n, client)


if __name__ == '__main__':
    start = time.perf_counter()
    main_sync()
    end = time.perf_counter()

    sync_duration = end - start
    print(f"Sync duration: {sync_duration}") # Sync duration: 5.671785291051492