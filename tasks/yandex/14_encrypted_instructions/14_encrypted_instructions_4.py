# data = '2[abc]3[cd]ef'
# data = '3[a]2[bc]'
data = '3[a2[c]]'

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
            print('---')
            print(position[0])
            print(position[1])
            print(len(data) - 1)
            print('---')
            if len(data) - 1 == position[1] and position[0] + 1 == position[1]:
                string = data[position[0]:]
                string = string.strip('[]')
            else:
                string = data[position[0]:position[1]]
            print(f'string: {string}')
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


arr = compile_arr(data)
print(process_data(arr))

