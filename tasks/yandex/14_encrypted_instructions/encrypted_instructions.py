# 113534713

import re
from typing import Optional, Tuple, Match


def read_data(filename: str) -> str:
    """Read and return first line from a specified file."""
    with open(filename, 'r') as file_in:
        return file_in.readline().strip()


def handle_brackets(char: str, position: int) -> int:
    """Adjust bracket nesting level based on the character provided."""
    if char == ']':
        position -= 1
    elif char == '[':
        position += 1
    return position


def process_string(multiplier: int, result: str, string: str) -> str:
    """Append string to result, repeated according to multiplier, handling
    nested patterns recursively.
    """
    if string.find('[') != -1 or string.find(']') != -1:
        result += process_data(string) * multiplier
    else:
        result += string * multiplier
    return result


def extract_multiplier(data: str, index: int) -> Tuple[int, int]:
    """Extract a numerical multiplier from the data string starting at the
    specified index.
    """
    match: Optional[Match[str]] = re.match(r'\d+', data[index:])
    if match:
        return int(match.group(0)), index + len(match.group(0))
    return 1, index


def is_natural_number(char: str) -> bool:
    return bool(re.match(r'^[1-9]\d*$', char))


def process_data(data: str) -> str:
    """Process the given string data, expanding nested patterns according to
    specified multipliers.
    """
    result: str = ''
    string: str = ''
    multiplier: int = 1
    position: int = 0

    index: int = 0
    while index < len(data):
        char = data[index]
        if is_natural_number(char) and not position:
            multiplier, index = extract_multiplier(data, index)
            continue
        position = handle_brackets(char, position)
        string += char

        if string and not position:
            if string[0] == '[' and string[-1] == ']':
                string = string[1:-1]

            result = process_string(multiplier, result, string)
            string = ''
            multiplier = 1
        index += 1

    return result


def main(input_filename: str):
    """Read data from a file, process it, and print the result."""
    data: str = read_data(input_filename)
    result: str = process_data(data)
    print(result)


if __name__ == '__main__':
    main(input_filename='input.txt')
