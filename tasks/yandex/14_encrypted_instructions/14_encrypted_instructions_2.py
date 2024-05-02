data = '1[a]3[ac]2[1[bc]2[a]]'

arr = [
    {
        'multiplier': 1,
        'inner_value': [
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
    }
]


idx = 0
def process_data(arr):
    for item in arr:
        if type(item['inner_value']) is list:
            process_data(item['inner_value'])
        else:
            print(item['multiplier'] * item['inner_value'])
        print(item['multiplier'])
        print(item['inner_value'])
        print('---')



process_data(arr)
