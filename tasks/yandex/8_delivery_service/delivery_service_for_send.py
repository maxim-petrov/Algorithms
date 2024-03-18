# 110053513

def read_data(filename: str, num_lines: int = 1):
    """Reads a specified number of lines from a file."""
    lines = []
    with open(filename, 'r') as file_in:
        try:
            for i in range(num_lines):
                lines.append(
                    next(file_in).strip()
                )
            return lines
        except StopIteration:
            return None


def main(input_filename: str):
    """Calculate and print the number of platforms needed for robots based on
    their weights and a weight limit.
    """
    try:
        data = read_data(input_filename, 2)
        robots_weights = sorted([int(weight) for weight in data[0].split()])
        weight_limit: int = int(data[1])

        platform_count: int = 0
        left: int = 0
        right: int = len(robots_weights) - 1

        while left <= right:
            total_weight: int = robots_weights[left] + robots_weights[right]

            if total_weight <= weight_limit:
                left += 1
            right -= 1
            platform_count += 1

        print(platform_count)
    except IOError:
        print("File not found or unable to read")


if __name__ == '__main__':
    main(input_filename='input.txt')
