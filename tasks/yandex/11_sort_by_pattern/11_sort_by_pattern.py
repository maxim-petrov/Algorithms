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


def sort_by_pattern(num_count, nums_to_sort, tmpl_array_length, tmpl_array):
    arr = []
    nums_to_sort_copy = nums_to_sort[:]

    for i in range(0, num_count):
        counter = 0
        if tmpl_array_length > i:
            while counter < num_count:
                if tmpl_array[i] == nums_to_sort[counter]:
                    arr.append(nums_to_sort[counter])
                    nums_to_sort_copy.remove(nums_to_sort[counter])
                counter += 1

    array = arr + sorted(nums_to_sort_copy)
    string = ' '.join(map(str, array))
    print(string)


@memory_profiler_decorator
@execution_time_decorator(num_runs=1)
@test_decorator
def main(input_filename: str):
    data = read_data(input_filename, 4)
    num_count, nums_to_sort, tmpl_array_length, tmpl_array = process_data(data)
    sort_by_pattern(num_count, nums_to_sort, tmpl_array_length, tmpl_array)


if __name__ == '__main__':
    main(input_filename='input.txt')
