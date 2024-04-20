# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

from decorators import ExecutionTimeDecorator
from decorators import TestDecorator
from decorators import MemoryProfilerDecorator

execution_time_decorator = ExecutionTimeDecorator
test_decorator = TestDecorator
memory_profiler_decorator = MemoryProfilerDecorator


def read_data(filename: str, num_lines: int = 2):
    """Reads a specified number of lines from a file."""
    lines = []
    with open(filename, 'r') as file_in:
        try:
            for i in range(num_lines):
                lines.append(
                    next(file_in).strip()
                )
            if num_lines == 1:
                return lines[0]
            return lines
        except StopIteration:
            return None


def counting_game(n, k):
    counter = 1
    numbers = list(range(1, n + 1))
    numbers_temp = numbers[:]
    while numbers_temp:
        for index, number in enumerate(numbers_temp):
            print(numbers)
            if counter == k:
                numbers.pop(index)
                counter = 1
                continue
            counter += 1


# @memory_profiler_decorator
# @execution_time_decorator(num_runs=1)
# @test_decorator
def main(input_filename: str):
    try:
        counting_game(5, 2)
    except IOError:
        print("File not found or unable to read")


if __name__ == '__main__':
    main(input_filename='input.txt')
