from decorators import ExecutionTimeDecorator
from decorators import TestDecorator
from decorators import MemoryProfilerDecorator

execution_time_decorator = ExecutionTimeDecorator
test_decorator = TestDecorator
memory_profiler_decorator = MemoryProfilerDecorator


@memory_profiler_decorator
@execution_time_decorator(num_runs=1)
@test_decorator
def main():  # Average execution time over 100 runs: 0.003326 seconds.
    with open('input.txt', 'r') as file_in:
        length = int(next(file_in).strip())
        arr_in = [int(char) for char in next(file_in).strip().split(' ')]
        data = list(set(arr_in))
        data.sort()
        while len(data) < length:
            data.append('_')
        print(' '.join(map(str, data)))


if __name__ == "__main__":
    main()
