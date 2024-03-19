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


def fibonacci_series(n, current_num=1):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 1
    result_sum = fibonacci_series(n - 1) + current_num
    return result_sum


# @memory_profiler_decorator
# @execution_time_decorator(num_runs=1)
# @test_decorator
def main(input_filename: str):
    """Calculate and print the number of platforms needed for robots based on
    their weights and a weight limit.
    """
    try:
        data = read_data(input_filename)
        print(fibonacci_series(4))
    except IOError:
        print("File not found or unable to read")


if __name__ == '__main__':
    main(input_filename='input.txt')
