# 10
# 8 5 5 8 6 9 8 2 4 7
# 8
# 9 8 1 1 1 5 10 8

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


def distribute_samples(order_count, min_weights, sample_count, sample_weights):
    counter = 0
    arr_temp = []
    for i in range(0, sample_count):
        for y in range(0, order_count):
            if sample_weights[i] == min_weights[y]:
                counter += 1
                break
            else:
                diff = sample_weights[i] - min_weights[y]
                if diff > 0:
                    arr_temp.append(min_weights[y])
        print(sample_weights[i])
        print(arr_temp)
        arr_temp = []

    print(counter)


def main(input_filename: str):
    data = read_data(input_filename, 4)
    order_count, min_weights, sample_count, sample_weights = process_data(data)
    distribute_samples(order_count, min_weights, sample_count, sample_weights)


if __name__ == '__main__':
    main(input_filename='input.txt')