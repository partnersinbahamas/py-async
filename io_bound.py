import httpx
import time

api_url = "https://api.github.com"

def get_outer_data(url: str) -> httpx.Response:
    return httpx.get(url=url)


def process_data(data: httpx.Response):
    numbers = sum([num**2 for num in range(1000)])
    return data.json()["current_user_url"], numbers

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_request = time.time()
    result = get_outer_data(api_url)

    request_duration = time.time() - start_request

    for key,value in result.json().items():
        print(f"{key}: {value}")
    print(f"Duration: {request_duration}")


    start_processing = time.time()
    data_result = get_outer_data(api_url)
    process_result = process_data(data_result)

    process_duration = time.time() - start_processing

    print(f"Result: {process_result}")
    print(f"Process duration: {process_duration}")
    print(request_duration / process_duration)

