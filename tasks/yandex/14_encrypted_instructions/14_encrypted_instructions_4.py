from itertools import islice

# data = '2[abc]3[cd]ef'
# data = '3[a]2[bc]'
# data = '3[a2[c]]'
# data = '3[2[c]]'


def read_data(filename: str, num_lines: int = 1):
    """Reads a specified number of lines from a file."""
    with open(filename, 'r') as file_in:
        try:
            lines = [line.strip() for line in islice(file_in, num_lines)]
            return lines
        except StopIteration:
            return None


def compile_arr(data):
    result = ''

    string = ''
    multiplier = 1

    position = 0
    for idx, char in enumerate(data):
        if char.isdigit() and not position:
            multiplier = int(char)
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
                result += compile_arr(string) * multiplier
            else:
                result += string * multiplier
            string = ''
            multiplier = 1

    return result



def process_data(arr):
    result = ''
    for item in arr:
        if type(item['inner_value']) is list:
            result += item['multiplier'] * process_data(item['inner_value'])
        else:
            result += item['multiplier'] * item['inner_value']
    return result



def main(input_filename: str):
    data = read_data(input_filename)
    arr = compile_arr(data)
    print(arr)


if __name__ == '__main__':
    main(input_filename='input.txt')
