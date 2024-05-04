import re
from typing import Optional, Match


def read_data(filename: str):
    """Read and return first line from a specified file."""
    with open(filename, 'r') as file_in:
        line: str = file_in.readline().strip()
        return line


def process_data(data: str):
    """Process the given string data, expanding nested patterns according to
    specified multipliers.
    """
    result: str = ''
    string: str = ''
    multiplier: int = 1

    position: int = 0
    for idx, char in enumerate(data):
        if char.isdigit() and not position:
            match: Optional[Match[str]] = re.match(r'\d+', data[idx:])
            if match and multiplier == 1:
                multiplier = int(match.group(0))
            continue
        elif char == ']':
            position -= 1
        elif char == '[':
            position += 1

        string += char

        if string and not position:
            if string[0] == '[' and string[-1] == ']':
                string = string[1:-1]

            if string.find('[') != -1 or string.find(']') != -1:
                result += process_data(string) * multiplier
            else:
                result += string * multiplier
            string = ''
            multiplier = 1

    return result


def main(input_filename: str):
    """Read data from a file, process it, and print the result."""
    data: str = read_data(input_filename)
    result: str = process_data(data)
    print(result)


if __name__ == '__main__':
    main(input_filename='input.txt')
