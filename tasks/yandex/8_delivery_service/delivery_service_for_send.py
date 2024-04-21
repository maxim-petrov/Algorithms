# 112547312

from typing import List, Optional
from itertools import islice


def read_data(filename: str, num_lines: int = 1) -> Optional[List[str]]:
    """Reads a specified number of lines from a file."""
    with open(filename, 'r') as file_in:
        try:
            lines = [line.strip() for line in islice(file_in, num_lines)]
            return lines
        except StopIteration:
            return None


def main(input_filename: str) -> None:
    """Calculate and print the number of platforms needed for robots based on
    their weights and a weight limit.
    """
    try:
        robots_weights: str
        weight_limit: str
        robots_weights, weight_limit = read_data(input_filename, 2)

        robots_weights: List[int] = sorted(
            [int(weight) for weight in robots_weights.split()]
        )
        weight_limit: int = int(weight_limit)

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
