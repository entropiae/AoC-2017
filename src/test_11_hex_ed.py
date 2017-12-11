from src.aoc_11_hex_ed import parse_raw_input, compute_final_distance, compute_positions


def test_part_1():
    test_cases = [
        ('ne,ne,ne', 3),
        ('ne,ne,sw,sw', 0),
        ('ne,ne,s,s', 2),
        ('se,sw,se,sw,sw', 3)
    ]

    for puzzle_raw_input, expected_output in test_cases:
        puzzle_input = parse_raw_input(puzzle_raw_input)
        positions = compute_positions(puzzle_input)
        assert compute_final_distance(positions) == expected_output
