from typing import List, Tuple

from src.utils import get_file_path

"""
As you walk through the door, a glowing humanoid shape yells in your direction.
"You there! Your state appears to be idle. Come help us repair the corruption in this spreadsheet - if we take another
millisecond, we'll have to display an hourglass cursor!"

The spreadsheet consists of rows of apparently-random numbers.
To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum.
For each row, determine the difference between the largest value and the smallest value;
the checksum is the sum of all of these differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8
The first row's largest and smallest values are 9 and 1, and their difference is 8.
The second row's largest and smallest values are 7 and 3, and their difference is 4.
The third row's difference is 6.
In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

What is the checksum for the spreadsheet in your puzzle input?
"""


def parse_input(raw_in: str) -> List[List[int]]:
    return [
        [int(value) for value in line.split('\t')]
        for line in raw_in.split('\n')
    ]


def compute_checksum(spreadsheet: List[List[int]]) -> int:
    max_min = [(max(row), min(row)) for row in spreadsheet]
    return sum(max_value - min_value for max_value, min_value in max_min)


def compute_evenly_divisible(spreadsheet: List[List[int]]) -> int:
    values = [
        extract_division_values(row)
        for row in spreadsheet
    ]
    return sum(dividend // divisor for dividend, divisor in values)


def extract_division_values(row: List[int]) -> Tuple[int, int]:
    for divisor in row:
        for dividend in row:
            if dividend != divisor and dividend % divisor == 0:
                return dividend, divisor


if __name__ == '__main__':
    input_file_path = get_file_path('corrupted_checksum_1.txt')

    with open(input_file_path) as f:
        raw_input = f.read()

    puzzle_input = parse_input(raw_input)
    checksum_output = compute_checksum(puzzle_input)
    print(f'Result for Part 1: {checksum_output}')
    evenly_divisible_output = compute_evenly_divisible(puzzle_input)
    print(f'Result for Part 2: {evenly_divisible_output}')
