from src.aoc_13_packet_scanners import compute_cost, parse_layer_configuration, compose_firewall_structure, get_ps_delay


def test_part_1():
    puzzle_input = compose_firewall_structure(
        parse_layer_configuration(
            ['0: 3', '1: 2', '4: 4', '6: 4']
        )
    )
    expected_cost = 24

    cost = compute_cost(puzzle_input)
    assert cost == expected_cost


def test_part_2():
    puzzle_input = parse_layer_configuration(
            ['0: 3', '1: 2', '4: 4', '6: 4']
    )
    expected_delay = 10

    delay = get_ps_delay(puzzle_input)
    assert delay == expected_delay