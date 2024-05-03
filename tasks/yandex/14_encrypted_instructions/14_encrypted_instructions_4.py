data = 'a2[b3[d]]c'

arr = [
    {
        'multiplier': 1,
        'inner_value': 'a'
    },
    {
        'multiplier': 3,
        'inner_value': 'ac'
    },
    {
        'multiplier': 2,
        'inner_value': [
            {
                'multiplier': 1,
                'inner_value': 'bc'
            },
            {
                'multiplier': 2,
                'inner_value': 'a'
            }
        ]
    }
]


def compile_arr(data):
    multiplier = ''

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
            if is_start and positions_temp:
                multiplier += char
                positions.append(positions_temp)
                positions_temp = []
        if char in '[':
            if not multiplier:
                multiplier = 1
            else:
                multiplier = int(multiplier)
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
    for position in positions:
        if not multiplier:
            multiplier = 1
        else:
            multiplier = int(multiplier)
        if len(position) == 1:
            string = data[position[0]]
            final.append({
                'multiplier': multiplier,
                'inner_value': string
            })
        else:
            string = data[position[0]:position[1]]
            if string.find('['):
                final.append({
                    'multiplier': multiplier,
                    'inner_value': compile_arr(string)
                })
                multiplier = ''
            else:
                final.append({
                    'multiplier': multiplier,
                    'inner_value': string
                })
                multiplier = ''
        print(string)
    return final

def process_data(arr):
    result = ''
    for item in arr:
        if type(item['inner_value']) is list:
            result += item['multiplier'] * process_data(item['inner_value'])
        else:
            result += item['multiplier'] * item['inner_value']
    return result


arr_2 = compile_arr(data)
print(process_data(arr_2))

