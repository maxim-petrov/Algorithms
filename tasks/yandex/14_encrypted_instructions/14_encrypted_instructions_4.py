data = '2[a]3[b]2[c]'

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
    arr = []

    string = ''
    multiplier = ''

    left, right = 0, 0
    for idx, char in enumerate(data):
        if char.isdigit() and left == 0:
            multiplier += char
            continue
        else:
            string += char

        if char == '[':
            left += 1

            if multiplier and left == 1:
                multiplier = int(multiplier)
            elif not multiplier and left == 1:
                multiplier = 1
        if char == ']':
            right += 1

            if left == 1 and right == 1:
                arr.append({
                    'multiplier': multiplier,
                    'inner_value': string.strip('[]')
                })
                left = 0
                right = 0
                string = ''
                multiplier = ''

    return arr

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
print(process_data(arr_2))
