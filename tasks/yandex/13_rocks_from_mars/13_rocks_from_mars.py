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
    min_weights.sort()
    sample_weights.sort()

    match_count = 0
    sample_index = 0

    for sample_weight in sample_weights:
        if sample_weight >= min_weights[sample_index]:
            match_count += 1
            sample_index += 1
            if match_count == order_count:
                break

    print(match_count)


@memory_profiler_decorator
@execution_time_decorator(num_runs=1)
@test_decorator
def main(input_filename: str):
    data = read_data(input_filename, 4)
    order_count, min_weights, sample_count, sample_weights = process_data(data)
    distribute_samples(order_count, min_weights, sample_count, sample_weights)


if __name__ == '__main__':
    main(input_filename='input.txt')