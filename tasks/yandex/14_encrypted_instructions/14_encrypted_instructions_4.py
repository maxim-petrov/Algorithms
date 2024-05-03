from itertools import islice

# data = '2[abc]3[cd]ef'
# data = '3[a]2[bc]'
data = '3[a2[c]]'


def read_data(filename: str, num_lines: int = 2):
    """Reads a specified number of lines from a file."""
    with open(filename, 'r') as file_in:
        try:
            lines = [line.strip() for line in islice(file_in, num_lines)]
            return lines
        except StopIteration:
            return None


def compile_arr(data):
    multiplier = ''
    multipliers = []

    final = []

    positions = []
    positions_temp = []
    num = 0
    is_start = True
    for i, char in enumerate(data):
        if char.isalpha() and is_start:
            positions_temp.append(i)
            if i == len(data) - 1:
                positions.append(positions_temp)
                positions_temp = []
            continue
        if char.isdigit():
            if is_start:
                multiplier += char
            if is_start and positions_temp:
                positions.append(positions_temp)
                positions_temp = []
        if char in '[':
            if not multiplier:
                multipliers.append(1)
            else:
                multipliers.append(int(multiplier))
            multiplier = ''
            is_start = False
            if num == 0:
                positions_temp.append(i + 1)
            num += 1
            continue
        if char in ']':
            is_start = False
            num -= 1
            if num == 0:
                positions_temp.append(i)
                positions.append(positions_temp)
                positions_temp = []
                is_start = True
            continue
    for i, position in enumerate(positions):
        multipliers.append(1)
        if len(position) == 1:
            string = data[position[0]]
            final.append({
                'multiplier': multipliers[i],
                'inner_value': string
            })
        else:
            if len(data) - 1 == position[1] and position[0] + 1 == position[1]:
                string = data[position[0]:]
                string = string.strip('[]')
            else:
                string = data[position[0]:position[1]]
            if string.find('[') != -1:
                final.append({
                    'multiplier': multipliers[i],
                    'inner_value': compile_arr(string)
                })
            else:
                final.append({
                    'multiplier': multipliers[i],
                    'inner_value': string
                })
    return final


def process_data(arr):
    result = ''
    for item in arr:
        if type(item['inner_value']) is list:
            result += item['multiplier'] * process_data(item['inner_value'])
        else:
            result += item['multiplier'] * item['inner_value']
    return result



def main(input_filename: str):
    # data = read_data(input_filename, 1)
    arr = compile_arr(data)
    print(process_data(arr))


if __name__ == '__main__':
    main(input_filename='input.txt')
