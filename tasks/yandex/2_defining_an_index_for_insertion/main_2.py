from decorators import ExecutionTimeDecorator
from decorators import TestDecorator
from decorators import MemoryProfilerDecorator
import time

execution_time_decorator = ExecutionTimeDecorator
test_decorator = TestDecorator
memory_profiler_decorator = MemoryProfilerDecorator


@memory_profiler_decorator
@execution_time_decorator(num_runs=1)
@test_decorator
def main():
    with open('input.txt', 'r') as file_in:
        numbers = tuple(
            int(number) for number in next(file_in).strip().split(' ')
        )
        target = int(next(file_in))

        while len(numbers) > 1:
            number_length = len(numbers) - 1
            diff = number_length % 2
            if diff:
                index = number_length // 2
            else:
                index = number_length // 2
            if numbers[number_length // 2] > target:
                numbers = numbers[:number_length // 2]
                index += number_length // 2
            else:
                numbers = numbers[number_length // 2:]
                index -= number_length // 2

        print(index)

if __name__ == '__main__':
    main()
