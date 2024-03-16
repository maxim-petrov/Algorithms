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

        if numbers_length < 2:
            result = False
            print(result)
            return

        is_peak_reached = False
        for number_index in range(0, numbers_length):
            if numbers[number_index] == numbers[number_index + 1]:
                result = False
                print(result)
                return
            if not is_peak_reached:
                if numbers[number_index] > numbers[number_index + 1]:
                    if number_index == 0:
                        result = False
                        print(result)
                        return
                    is_peak_reached = True
            else:
                if numbers[number_index] < numbers[number_index + 1]:
                    result = False
                    print(result)
                    return
        result = True
        print(result)


if __name__ == '__main__':
    main(input_filename='input.txt')
