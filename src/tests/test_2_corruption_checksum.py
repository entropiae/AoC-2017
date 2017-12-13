from src.aoc_2_corruption_checksum import parse_input, compute_checksum, compute_evenly_divisible


def test_parse_input():
    provided_input = """179	2358	5197	867\n2637	136	3222	591"""
    expected_output = [
        [179, 2358, 5197, 867],
        [2637, 136, 3222, 591],
    ]
    output = parse_input(provided_input)
    assert output == expected_output


def test_corruption_checksum():
    provided_input = [
        [5, 1, 9, 5],
        [7, 5, 3],
        [2, 4, 6, 8]
    ]
    expected_output = 18
    output = compute_checksum(provided_input)
    assert output == expected_output


def test_evenly_divisible():
    provided_input = [
        [5, 9, 2, 8],
        [9, 4, 7, 3],
        [3, 8, 6, 5]
    ]
    expected_output = 9
    output = compute_evenly_divisible(provided_input)
    assert output == expected_output
