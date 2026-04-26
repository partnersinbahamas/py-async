import time
from decimal import Decimal
from typing import List

IntDividers = List[int]

FILE_NAME = "dividers.txt"

def factorize_single(number: int) -> IntDividers:
    return [n for n in range(1, number + 1) if number % n == 0]


def write_into_disc(
        number: int,
        dividers: IntDividers,
        file_name: str = FILE_NAME,
) -> None:
    content = f"{str(number)}: {', '.join(map(str, dividers))}\n"

    with open(file_name, "a+") as writer:
        writer.writelines(content)



def calculate_cpu_bound(numbers: IntDividers, file_name: str = FILE_NAME):
    cpu_time = 0
    write_time = 0

    for number in numbers:
        start_time = time.time()
        result = factorize_single(number)
        end_time = time.time()

        duration_diff = end_time - start_time
        cpu_time += duration_diff

        start_time = time.time()
        write_into_disc(number, result, file_name=file_name)
        end_time = time.time()

        duration_write = end_time - start_time
        write_time += duration_write

        print(
            f"Number: {number}, "
            f"CPU time: {duration_diff:<20.6f}, "
            f"Write time: {duration_write:<20.6f}"
        )

    print(
        f"CPU time: {cpu_time:>20.6f}, "
        f"Write time: {write_time:>20.6f}"
    )

if __name__ == '__main__':
    numbers = [10, 115, 4567, 10543, 123457, 6834013]
    calculate_cpu_bound(numbers)