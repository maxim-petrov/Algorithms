# 10
# 2 4 3 5 6 0 9 8 7 7
# 6
# 2 4 3 5 6 0

# 2 4 3 5 6 0 7 7 8 9

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
    return (
        int(data[0]),
        [int(num) for num in data[1].split()],
        int(data[2]),
        [int(num) for num in data[3].split()]
    )


def sort_by_pattern(num_count, nums_to_sort, tmpl_array_length, tmpl_array):
    arr = nums_to_sort[:]
    for i in range(0, num_count):
        for y in range(i, num_count):
            if y < tmpl_array_length:
                if tmpl_array[i] == nums_to_sort[y]:
                    print(arr[i])
                    print(tmpl_array[i])
    print(arr)


def main(input_filename: str):
    data = read_data(input_filename, 4)
    num_count, nums_to_sort, tmpl_array_length, tmpl_array = process_data(data)
    sort_by_pattern(num_count, nums_to_sort, tmpl_array_length, tmpl_array)


if __name__ == '__main__':
    main(input_filename='input.txt')
