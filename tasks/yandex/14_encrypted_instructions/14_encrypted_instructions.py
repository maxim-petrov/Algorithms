from itertools import islice


def read_data(filename: str, num_lines: int = 2):
    """Reads a specified number of lines from a file."""
    with open(filename, 'r') as file_in:
        try:
            lines = [line.strip() for line in islice(file_in, num_lines)]
            return lines
        except StopIteration:
            return None


def process_data(data):
    return data[0]


def decode_instruction(instruction):
    arr = []
    arr_temp = ''

    multiplier = 1
    multiplier_temp = ''

    left, right = 0, 0
    for idx, char in enumerate(instruction):
        if char.isalpha():
            arr_temp += char
        if char.isdigit():
            multiplier_temp += char
        if char == '[':
            arr += arr_temp * multiplier
            arr_temp = ''
            if multiplier_temp and left == right:
                multiplier = int(multiplier_temp)
                multiplier_temp = ''
            left += 1
        if char == ']':
            right += 1
            if left == right:
                arr += arr_temp * multiplier
                arr_temp = ''
                multiplier = 1
    arr += arr_temp * multiplier

    print(instruction)
    print(arr)

def main(input_filename: str):
    data = read_data(input_filename, 1)
    command = process_data(data)
    decode_instruction(command)


if __name__ == '__main__':
    main(input_filename='input.txt')
