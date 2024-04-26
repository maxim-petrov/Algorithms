from itertools import islice

from decorators import ExecutionTimeDecorator
from decorators import TestDecorator
from decorators import MemoryProfilerDecorator

execution_time_decorator = ExecutionTimeDecorator
test_decorator = TestDecorator
memory_profiler_decorator = MemoryProfilerDecorator


def read_data(filename: str, num_lines: int = 2):
    """Reads a specified number of lines from a file."""
    with open(filename, 'r') as file_in:
        try:
            lines = [line.strip() for line in islice(file_in, num_lines)]
            return lines
        except StopIteration:
            return None


def counting_game(n, k):
    counter = 1
    numbers = list(range(1, n + 1))
    while len(numbers) > 1:
        for number in numbers[:]:
            if len(numbers) > 1:
                if counter >= k:
                    numbers.remove(number)
                    counter = 1
                else:
                    counter += 1
    print(numbers[0])


@memory_profiler_decorator
@execution_time_decorator(num_runs=1)
@test_decorator
def main(input_filename: str):
    try:
        n, k = map(int, read_data(input_filename, 2))
        counting_game(n, k)
    except IOError:
        print("File not found or unable to read")


if __name__ == '__main__':
    main(input_filename='input.txt')
