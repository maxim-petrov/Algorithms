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


def process_data(data):
    return (
        int(data[0]),
        [int(num) for num in data[1].split()],
        int(data[2]),
        [int(num) for num in data[3].split()]
    )


def distribute_samples(order_count, min_weights, sample_count, sample_weights):
    counter = 0
    temp_arr = []
    for i in range(0, order_count):
        for y in range(0, sample_count):
            if min_weights[i] == sample_weights[y]:
                temp_arr.append(sample_weights[y])
                sample_weights[y] = 0
                min_weights[i] = 10000
                counter += 1
                break
    for i in range(0, order_count):
        for y in range(0, sample_count):
            if min_weights[i] < sample_weights[y]:
                sample_weights[y] = 0
                min_weights[i] = 10000
                counter += 1
                break
    print(counter)


@memory_profiler_decorator
@execution_time_decorator(num_runs=1)
@test_decorator
def main(input_filename: str):
    data = read_data(input_filename, 4)
    order_count, min_weights, sample_count, sample_weights = process_data(data)
    distribute_samples(order_count, min_weights, sample_count, sample_weights)


if __name__ == '__main__':
    main(input_filename='input.txt')