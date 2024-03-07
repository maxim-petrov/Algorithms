import os
from contextlib import redirect_stdout
import io


class TestDecorator:
    def __init__(self, func):
        self.func = func
        self.__name__ = func.__name__

    def __call__(self, *args, **kwargs):
        test_cases = read_test_cases()
        all_tests_passed = True

        for input_data, expected_output in test_cases:
            if not run_test_case(input_data, expected_output, self.func):
                print("Stopping due to failed test.")
                all_tests_passed = False
                break

        if all_tests_passed:
            print("All tests passed successfully.")

        if os.path.exists('input_temp.txt'):
            os.remove('input_temp.txt')
        if os.path.exists('temp_output.txt'):
            os.remove('temp_output.txt')


def run_test_case(input_data, expected_output, func, *args, **kwargs):
    with open('input_temp.txt', 'w') as file:
        file.write(input_data)

    captured_output = io.StringIO()
    with redirect_stdout(captured_output):
        func(input_filename='input_temp.txt', *args, **kwargs)

    output = captured_output.getvalue().strip()
    if output == expected_output:
        print(f"Test passed.")
    else:
        print(f"Test failed.\nInput: {input_data}\nOutput: {output}\nExpected: {expected_output}")
        return False
    return True


def read_test_cases():
    with open('input.txt', 'r') as file:
        inputs = file.read().strip().split('---')
    with open('answer.txt', 'r') as file:
        answers = file.read().strip().split('---')

    return [(input.strip(), answer.strip()) for input, answer in
            zip(inputs, answers)]