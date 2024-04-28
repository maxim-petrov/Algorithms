# 3 2 0 1 4 6 5

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
        [int(num) for num in data[1].split()]
    )


def block_merge_sort(num_count, nums_to_sort):
    result = 0
    subtractor = 0
    maximum = 0
    count = []
    for i in range(0, num_count):
        if len(count) - 1 < maximum:
            count.append(nums_to_sort[i])
            if nums_to_sort[i] - subtractor > maximum:
                maximum = nums_to_sort[i] - subtractor
        else:
            result += 1
            maximum += subtractor
            subtractor = maximum + 1
            maximum = 0
            count = []
            if len(count) - 1 < maximum:
                count.append(nums_to_sort[i])
                if nums_to_sort[i] - subtractor > maximum:
                    maximum = nums_to_sort[i] - subtractor
    result += 1
    print(result)


def main(input_filename: str):
    data = read_data(input_filename, 2)
    num_count, nums_to_sort = process_data(data)
    block_merge_sort(num_count, nums_to_sort)


if __name__ == '__main__':
    main(input_filename='input.txt')
