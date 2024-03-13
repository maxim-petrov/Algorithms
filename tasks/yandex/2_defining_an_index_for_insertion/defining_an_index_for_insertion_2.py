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
        target = int(next(file_in))

        left = 0
        right = len(numbers)

        while left < right:
            mid = (left + right) // 2

            if numbers[mid] < target:
                left = mid + 1
            else:
                right = mid

        print(left)


if __name__ == '__main__':
    main(input_filename='input.txt')
