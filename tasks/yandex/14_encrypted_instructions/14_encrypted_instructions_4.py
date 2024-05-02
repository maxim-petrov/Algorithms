data = '2[2[c]]2[a]'

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
    multiplier = 1
    start = data.find('[')

    if start != -1 and start > 0:
        multiplier = int(data[:start])

    positions = []

    num = 0
    for i, char in enumerate(data):
        if char in '[':
            positions.append((char, num))
            num += 1
        if char in ']':
            num -= 1
            positions.append((char, num))

    print(positions)





def process_data(arr):
    result = ''
    for item in arr:
        if type(item['inner_value']) is list:
            result += item['multiplier'] * process_data(item['inner_value'])
        else:
            result += item['multiplier'] * item['inner_value']
    return result


arr_2 = compile_arr(data)
print(arr_2)

