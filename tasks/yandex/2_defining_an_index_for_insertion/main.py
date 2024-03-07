from decorators import ExecutionTimeDecorator
from decorators import TestDecorator
from decorators import MemoryProfilerDecorator

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

        indexed_numbers = enumerate(numbers)
        for index, number in indexed_numbers:
            if target <= number:
                output = index
                break
            output = index + 1

        print(output)


if __name__ == '__main__':
    main()
