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
        data_arr = tuple(read_next_line(input_filename).strip())
        data_arr_length = len(data_arr)
        if data_arr_length % 2:
            print(False)
            return

        left = 0
        left_index = 0
        for right_index in range(1, data_arr_length):
            if left_index < left:
                left_index = right_index - 1
                left = right_index

            left_bracket = data_arr[left_index]
            right_bracket = data_arr[right_index]
            matching_pairs = {('{', '}'), ('[', ']'), ('(', ')')}
            if right_bracket in {pair[1] for pair in matching_pairs}:
                if (left_bracket, right_bracket) in matching_pairs:
                    left_index -= 1
                    continue
                else:
                    print(False)
                    return
            left_index += 1

        if left_index < left or left_index == 0:
            print(True)
        else:
            print(False)

    except IOError:
        print("File not found or unable to read")


if __name__ == '__main__':
    main(input_filename='input.txt')
