from src.aoc_16_permutation_promenade import make_program_dance, _spin, _exchange, _partner


def test_part_1():
    programs_start = 'abcde'
    moves = [('s', ['1']), ('x', ['3', '4']), ('p', ['e', 'b'])]
    output = make_program_dance(programs_start, moves)

    assert output == 'baedc'


def test_spin():
    programs_start = list('abcde')
    output = _spin(programs_start, 3)

    assert ''.join(output) == 'cdeab'


def test_exchange():
    programs_start = list('eabcd')
    output = _exchange(programs_start, 3, 4)

    assert ''.join(output) == 'eabdc'


def test_partner():
    programs_start = list('eabdc')
    output = _partner(programs_start, 'e', 'b')

    assert ''.join(output) == 'baedc'
