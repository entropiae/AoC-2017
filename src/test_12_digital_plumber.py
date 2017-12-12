from src.aoc_12_digital_plumber import retrieve_linked_programs, count_total_groups

group_definitions = {
    0: [2],
    1: [1],
    2: [0, 3, 4],
    3: [2, 4],
    4: [2, 3, 6],
    5: [6],
    6: [4, 5]
}


def test_count():
    assert len(set(retrieve_linked_programs(0, group_definitions))) == 6


def test_count_groups():
    assert (count_total_groups(group_definitions)) == 2
