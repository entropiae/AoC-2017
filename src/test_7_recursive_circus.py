from src.aoc_7_recursive_circus import parse_row, find_tree_root


def test_parse_long_row():
    long_row = 'tzdmi (891) -> mhzwwo, mgybhs, pptdd'
    expected_output = 'tzdmi', 891, ['mhzwwo', 'mgybhs', 'pptdd']

    output = parse_row(long_row)

    assert output == expected_output


def test_parse_short_row():
    short_row = 'tzdmi (891)'
    expected_output = 'tzdmi', 891, []

    output = parse_row(short_row)

    assert output == expected_output


def test_find_root_node():
    puzzle_input = [
        ('pbga', 66, []),
        ('xhth', 57, []),
        ('ebii', 61, []),
        ('havc', 66, []),
        ('ktlj', 57, []),
        ('fwft', 72, ['ktlj', 'cntj', 'xhth']),
        ('qoyq', 66, []),
        ('padx', 45, ['pbga', 'havc', 'qoyq']),
        ('tknk', 41, ['ugml', 'padx', 'fwft']),
        ('jptl', 61, []),
        ('ugml', 68, ['gyxo', 'ebii', 'jptl']),
        ('gyxo', 61, []),
        ('cntj', 57, []),
    ]
    expected_root = 'tknk'
    root = find_tree_root(puzzle_input)
    assert expected_root == root
