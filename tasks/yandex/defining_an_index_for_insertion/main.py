from decorators import ExecutionTimeDecorator, TestDecorator

execution_time_decorator = ExecutionTimeDecorator
test_decorator = TestDecorator


@execution_time_decorator
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
