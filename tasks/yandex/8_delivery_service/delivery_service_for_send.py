# 112653135

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


def process_data(robots_weights, weight_limit):
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

    return platform_count


def main() -> None:
    """Calculate and print the number of platforms needed for robots based on
    their weights and a weight limit.
    """
    robots_weights, weight_limit = read_data('input.txt', 2)

    platform_count = process_data(robots_weights, weight_limit)

    print(platform_count)


if __name__ == '__main__':
    main()
