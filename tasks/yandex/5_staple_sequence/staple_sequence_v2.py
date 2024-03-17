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


def is_correct_bracket_sequence(bracket_sequence):
    matching_pairs = {('{', '}'), ('[', ']'), ('(', ')')}

    if len(bracket_sequence) % 2:
        return False

    stack = []
    while len(bracket_sequence):
        current_bracket = bracket_sequence.pop()
        if len(stack) and (current_bracket, stack[-1]) in matching_pairs:
            stack.pop()
        else:
            stack.append(current_bracket)
    return len(stack) == 0


@memory_profiler_decorator
@execution_time_decorator(num_runs=1)
@test_decorator
def main(input_filename):
    try:
        bracket_sequence = list(read_next_line(input_filename).strip())
        result = is_correct_bracket_sequence(bracket_sequence)
        print(result)
    except IOError:
        print("File not found or unable to read")


if __name__ == '__main__':
    main(input_filename='input.txt')
