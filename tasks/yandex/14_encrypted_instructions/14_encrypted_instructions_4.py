data = '2[a]3[b]2[c]'

arr = [
    {
        'multiplier': 2,
        'inner_value': [
            {
                'multiplier': 2,
                'inner_value': 'a'
            },
            {
                'multiplier': 2,
                'inner_value': 'c'
            },
        ]
    },
    {
        'multiplier': 3,
        'inner_value': 'b'
    },
    {
        'multiplier': 2,
        'inner_value': 'c'
    }
]


def process_data(arr):
    result = ''
    for item in arr:
        if type(item['inner_value']) is list:
            result += item['multiplier'] * process_data(item['inner_value'])
        else:
            result += item['multiplier'] * item['inner_value']
    return result


print(process_data(arr))
