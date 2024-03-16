from decorators import ExecutionTimeDecorator
from decorators import TestDecorator
from decorators import MemoryProfilerDecorator

execution_time_decorator = ExecutionTimeDecorator
test_decorator = TestDecorator
memory_profiler_decorator = MemoryProfilerDecorator


@memory_profiler_decorator
@execution_time_decorator(num_runs=1)
@test_decorator
def main(input_filename):
    with open(input_filename, 'r') as file_in:
        numbers = tuple(
            int(number) for number in next(file_in).strip().split(' ')
        )
        numbers_length = len(numbers) - 1

        if numbers_length >= 2:
            result = check_if_mountain_sequence(numbers, numbers_length)
        else:
            result = False

        print(result)


def check_if_mountain_sequence(numbers, numbers_length):
    is_peak_reached = False
    for number_index in range(0, numbers_length):
        current_number = numbers[number_index]
        next_number = numbers[number_index + 1]

        if current_number == next_number:
            return False
        elif not is_peak_reached:
            if current_number > next_number:
                if number_index == 0:
                    return False
                is_peak_reached = True
        else:
            if current_number < next_number:
                return False
    if is_peak_reached:
        return True
    else:
        return False


if __name__ == '__main__':
    main(input_filename='input.txt')
