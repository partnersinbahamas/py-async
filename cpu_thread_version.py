import time
from typing import Sequence
import threading

SequenceInt = Sequence[int]

numbers: SequenceInt = (
  567456, 8347291, 672345, 9182734, 745612,
  8392017, 654321, 7123984, 598234, 8761235,
  923456, 7812346, 645789, 8345672, 712345,
  9982341, 623451, 7459823, 812345, 9345671,
  567891, 6782345, 789123, 8456723, 912345,
  7345612, 623789, 8561234, 945678, 7123985
)

def factorize_single(number: int):
  return [n for n in range(1, number + 1) if number % n == 0]

def factorize_single_print(index: int, number: int):
  print(f"Start task for #{index} with {number}")
  dividers = factorize_single(number)

  print(f"Result: {dividers}")


def main_threads():
    tasks = []
    for index, number in enumerate(numbers):
        tasks.append(threading.Thread(target=factorize_single_print, args=(index, number)))
        tasks[-1].start()

    for task in tasks:
        task.join()


if __name__ == '__main__':
  start = time.perf_counter()
  main_threads()

  end = time.perf_counter()
  duration = end - start

  print(f"CPU Threads duration: {duration}") # CPU Threads duration: 3.1385266659781337