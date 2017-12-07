from src.aoc_6_memory_reallocation import cycles_before_infinite_loops


def test_part_1():
    provided_input = [0, 2, 7, 0]
    expected_output = 5

    output, _ = cycles_before_infinite_loops(provided_input)
    assert output == expected_output
