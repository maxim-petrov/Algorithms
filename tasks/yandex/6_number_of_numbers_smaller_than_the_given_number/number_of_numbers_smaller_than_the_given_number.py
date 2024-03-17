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


# @memory_profiler_decorator
# @execution_time_decorator(num_runs=1)
# @test_decorator
def main(input_filename):
    try:
        data = list(read_next_line(input_filename).strip().split())
        result_array = []
        for first_index, first_value in enumerate(data):
            current_value = 0
            for second_index, second_value in enumerate(data):
                if first_index == second_index:
                    continue
                if int(first_value) > int(second_value):
                    current_value += 1
            result_array.append(current_value)
        result = ' '.join(map(str, result_array))
        print(result)
    except IOError:
        print("File not found or unable to read")


if __name__ == '__main__':
    main(input_filename='input.txt')
