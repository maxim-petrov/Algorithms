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
        data_arr = tuple(read_next_line(input_filename).strip())
        data_arr_length = len(data_arr)
        if data_arr_length % 2:
            return False

        left = 0
        left_index = 0
        for right_index in range(1, data_arr_length):
            if left_index < left:
                left_index = right_index - 1
                left = right_index
            if data_arr[right_index] == '}':
                if data_arr[left_index] != '{':
                    print(False)
                    return
                else:
                    left_index -= 1
                    continue
            if data_arr[right_index] == ']':
                if data_arr[left_index] != '[':
                    print(False)
                    return
                else:
                    left_index -= 1
                    continue
            if data_arr[right_index] == ')':
                if data_arr[left_index] != '(':
                    print(False)
                    return
                else:
                    left_index -= 1
                    continue
            left_index += 1
        print(True)


    except IOError:
        print("File not found or unable to read")


if __name__ == '__main__':
    main(input_filename='input.txt')