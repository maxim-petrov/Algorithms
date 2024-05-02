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
    string = ''
    left, right = 0, 0
    for char in instruction:
        if char == '[':
            left += 1
            if left - right != 1:
                string += char
            continue
        if char == ']':
            right += 1
            if left - right:
                string += char
            continue
        if left != right:
            string += char
            continue
        if left == right:
            arr.append(string)
    print(arr)
    print(string)



def main(input_filename: str):
    data = read_data(input_filename, 1)
    command = process_data(data)
    decode_instruction(command)


if __name__ == '__main__':
    main(input_filename='input.txt')
