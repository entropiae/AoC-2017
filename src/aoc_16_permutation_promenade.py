import string
from functools import reduce

from src.utils import read_first_line

"""
--- Day 16: Permutation Promenade ---

You come upon a very unusual sight; a group of programs here appear to be
dancing.

There are sixteen programs in total, named a through p. They start by
standing in a line: a stands in position 0, b stands in position 1, and
so on until p, which stands in position 15.

The programs' dance consists of a sequence of dance moves:

 - Spin, written sX, makes X programs move from the end to the front,
   but maintain their order otherwise. (For example, s3 on abcde
   produces cdeab).
 - Exchange, written xA/B, makes the programs at positions A and B swap
   places.
 - Partner, written pA/B, makes the programs named A and B swap places.

For example, with only five programs standing in a line (abcde), they
could do the following dance:

 - s1, a spin of size 1: eabcd.
 - x3/4, swapping the last two programs: eabdc.
 - pe/b, swapping programs e and b: baedc.

After finishing their dance, the programs end up in order baedc.

You watch the dance for a while and record their dance moves (your puzzle
input). In what order are the programs standing after their dance?

--- Part Two ---

Now that you're starting to get a feel for the dance moves, you turn 
your attention to the dance as a whole.

Keeping the positions they ended up in from their previous dance, the 
programs perform it again and again: including the first dance, a total 
of one billion (1000000000) times.

In the example above, their second dance would begin with the order baedc, 
and use the same dance moves:

 - s1, a spin of size 1: cbaed.
 - x3/4, swapping the last two programs: cbade.
 - pe/b, swapping programs e and b: ceadb.

In what order are the programs standing after their billion dances?
"""


def make_program_dance(start, moves):
    return ''.join(reduce(_do_move, moves, list(start)))


def _do_move(program_position, move):
    move_to_perform, params = move
    return available_moves[move_to_perform](program_position, *params)


def _spin(xs, num_programs):
    num_programs = int(num_programs)
    return xs[-num_programs:] + xs[:-num_programs]


def _exchange(xs, a, b):
    a = int(a)
    b = int(b)
    xs = list(xs)
    xs[a], xs[b] = xs[b], xs[a]
    return xs


def _partner(xs, a, b):
    idxs = dict((p, idx) for idx, p in enumerate(xs))
    return _exchange(xs, idxs[a], idxs[b])


available_moves = {
    's': _spin,
    'x': _exchange,
    'p': _partner
}


def parse_input(raw):
    commands = raw.split(',')
    return [(c[0], c[1:].split('/')) for c in commands]


if __name__ == '__main__':
    puzzle_input = parse_input(read_first_line('permutation_promenade.txt'))
    after_moves = make_program_dance(string.ascii_lowercase[:16], puzzle_input)
    print(f'Result for Part 1: {after_moves}')

    for idx in range(999_999_999 % 60):  # output repeat itself after 60 iterations :)
        after_moves = make_program_dance(after_moves, puzzle_input)

    print(f'Result for Part 2: {after_moves}')
