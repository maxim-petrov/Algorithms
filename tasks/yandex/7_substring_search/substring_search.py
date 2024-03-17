from decorators import ExecutionTimeDecorator
from decorators import TestDecorator
from decorators import MemoryProfilerDecorator

execution_time_decorator = ExecutionTimeDecorator
test_decorator = TestDecorator
memory_profiler_decorator = MemoryProfilerDecorator


def read_next_line(filename):
    with open(filename, 'r') as file_in:
        try:
            return next(file_in)
        except StopIteration:
            return None


@memory_profiler_decorator
@execution_time_decorator(num_runs=1)
@test_decorator
def main(input_filename):
    try:
        data = list(read_next_line(input_filename).strip())
        left_index = 0
        elements_in_slice = 1
        result = 0
        for index in range(0, len(data)):
            window = data[left_index:elements_in_slice + left_index]
            window_set = set(window)
            if len(window) == len(window_set):
                elements_in_slice += 1
                result += 1
            else:
                left_index += 1
        print(result)
    except IOError:
        print("File not found or unable to read")


if __name__ == '__main__':
    main(input_filename='input.txt')
