# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

from decorators import ExecutionTimeDecorator
from decorators import TestDecorator
from decorators import MemoryProfilerDecorator

execution_time_decorator = ExecutionTimeDecorator
test_decorator = TestDecorator
memory_profiler_decorator = MemoryProfilerDecorator


def read_data(filename: str, num_lines: int = 1):
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


fibonacci_array = []


def fibonacci_series(target, number=0, next_number=1):
    if number:
        fibonacci_array.append(number)
    if not target:
        fibonacci_array.append(1)
        return
    if number < target:
        prev_number_temp = number
        number = next_number
        next_number += prev_number_temp
        fibonacci_series(target, number, next_number)


@memory_profiler_decorator
@execution_time_decorator(num_runs=1)
@test_decorator
def main(input_filename: str):
    try:
        data = int(read_data(input_filename))
        fibonacci_series(data)
        print(fibonacci_array[-1])
    except IOError:
        print("File not found or unable to read")


if __name__ == '__main__':
    main(input_filename='input.txt')
