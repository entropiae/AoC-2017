from src.aoc_8_you_like_registers import parse_input, eval_row, get_max_values


def test_part_1():
    rules = [
        'b inc 5 if a > 1',
        'a inc 1 if b < 5',
        'c dec -10 if a >= 1',
        'c inc -20 if c == 10',
    ]
    instructions = [eval_row(row) for row in parse_input(rules)]
    max_value, _ = get_max_values(instructions)
    assert max_value == 1


def test_part_2():
    rules = [
        'b inc 5 if a > 1',
        'a inc 1 if b < 5',
        'c dec -10 if a >= 1',
        'c inc -20 if c == 10',
    ]
    instructions = [eval_row(row) for row in parse_input(rules)]
    _, absolute_max_value = get_max_values(instructions)
    assert absolute_max_value == 10
