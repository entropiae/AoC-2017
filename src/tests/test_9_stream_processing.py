from src.aoc_9_stream_processing import filter_deletions, filter_garbage, count, count_groups, count_garbage


def test_filter_deletion():
    assert '<{}>' == ''.join(filter_deletions('<{!>}>'))
    assert '<>' == ''.join(filter_deletions('<!!>'))
    assert '<>' == ''.join(filter_deletions('<>'))
    assert '<{o"i,<{i<a>' == ''.join(filter_deletions('<{o"i!a,<{i<a>'))


def test_filter_garbage():
    assert '{{},{},{},{}}' == ''.join(filter_garbage('{{<a>},{<a>},{<a>},{<a>}}'))
    assert '{,,,}' == ''.join(filter_garbage('{<a>,<a>,<a>,<a>}'))


def test_count():
    assert count('{}') == 1
    assert count('{{{}}}') == 6
    assert count('{{{}{}{{}}}}') == 16


def test_part_1():
    assert count_groups('{{<ab>},{<ab>},{<ab>},{<ab>}}') == 9
    assert count_groups('{{<!!>},{<!!>},{<!!>},{<!!>}}') == 9
    assert count_groups('{{<a!>},{<a!>},{<a!>},{<ab>}}') == 3


def test_part_2():
    assert count_garbage('<>') == 0
    assert count_garbage('<<<<>') == 3
    assert count_garbage('<{!>}>') == 2
    assert count_garbage('<!!>') == 0
    assert count_garbage('<!!!>>') == 0
    assert count_garbage('<{o"i!a,<{i<a>') == 10
