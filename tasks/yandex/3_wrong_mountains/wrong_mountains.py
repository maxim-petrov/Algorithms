from decorators import ExecutionTimeDecorator
from decorators import TestDecorator
from decorators import MemoryProfilerDecorator

execution_time_decorator = ExecutionTimeDecorator
test_decorator = TestDecorator
memory_profiler_decorator = MemoryProfilerDecorator


def read_numbers_from_file(filename):
    with open(filename, 'r') as file_in:
        numbers = tuple(
            int(number) for number in next(file_in).strip().split()
        )
    return numbers


def is_mountain_sequence(numbers):
    numbers_length = len(numbers)

    if numbers_length < 3:
        return False

    is_peak_found = False
    for number_index in range(0, numbers_length - 1):
        current_number = numbers[number_index]
        next_number = numbers[number_index + 1]

        if current_number == next_number:
            return False
        elif current_number > next_number:
            if not number_index:
                return False
            if not is_peak_found:
                is_peak_found = True
        elif is_peak_found:
            return False

    return is_peak_found


@memory_profiler_decorator
@execution_time_decorator(num_runs=1)
@test_decorator
def main(input_filename):
    try:
        numbers = read_numbers_from_file(input_filename)
        result = is_mountain_sequence(numbers)
        print(result)
    except IOError:
        print("File not found or unable to read")


if __name__ == '__main__':
    main(input_filename='input.txt')
