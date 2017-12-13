from src.aoc_13_packet_scanners import compute_cost


def test_part_1():
    puzzle_input = ['0: 3', '1: 2', '4: 4', '6: 4']
    expected_cost = 24

    cost = compute_cost(puzzle_input)
    assert cost == expected_cost
