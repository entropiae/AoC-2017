from typing import Dict, List

from src.utils import read_first_line, compute_coordinates_from_steps, Step, Points, Point
from functools import reduce

"""
--- Day 11: Hex Ed ---

Crossing the bridge, you've barely reached the other side of the stream
when a program comes up to you, clearly in distress. "It's my child
process," she says, "he's gotten lost in an infinite grid!"

Fortunately for her, you have plenty of experience with infinite grids.

Unfortunately for you, it's a hex grid.

The hexagons ("hexes") in this grid are aligned such that adjacent hexes
can be found to the north, northeast, southeast, south, southwest, and
northwest:

  \ n  /
nw +--+ ne
  /    \
-+      +-
  \    /
sw +--+ se
  / s  \

You have the path the child process took. Starting where he started, you
need to determine the fewest number of steps required to reach him. (A
"step" means to move from the hex you are in to any adjacent hex.)

For example:

 - ne,ne,ne is 3 steps away.
 - ne,ne,sw,sw is 0 steps away (back where you started).
 - ne,ne,s,s is 2 steps away (se,se).
 - se,sw,se,sw,sw is 3 steps away (s,s,sw).
 
--- Part Two ---

How many steps away is the furthest he ever got from his starting 
position?
"""

direction_to_step: Dict[str, Step] = {
    'n': (1, 0),
    'ne': (1, -1),
    'se': (0, -1),
    's': (-1, 0),
    'sw': (-1, 1),
    'nw': (0, 1)
}


def compute_final_distance(points: Points) -> int:
    return hex_distance((0, 0), points[-1])


def compute_max_distance(point: Points) -> int:
    return max(hex_distance((0, 0), p) for p in point)


def compute_positions(directions: List[str]) -> Points:
    steps = (direction_to_step[d] for d in directions)
    return reduce(compute_next_position, steps, [(0, 0)])


def compute_next_position(acc: Points, step: Step) -> Points:
    start = acc[-1]
    position = compute_coordinates_from_steps(start, step)
    acc.append(position)
    return acc


def parse_raw_input(raw: str) -> List[str]:
    return raw.split(',')


def hex_distance(p1: Point, p2: Point) -> int:
    x1, y1 = p1
    x2, y2 = p2

    dx = x2 - x1
    dy = y2 - y1

    if sign(dx) == sign(dy):
        d = abs(dx + dy)
    else:
        d = max(abs(dx), abs(dy))
    return d


def sign(x: int) -> int:
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


if __name__ == '__main__':
    raw_puzzle_input = read_first_line('hex_ed.txt')
    puzzle_input = parse_raw_input(raw_puzzle_input)

    positions = compute_positions(puzzle_input)
    final_distance = compute_final_distance(positions)
    max_distance = compute_max_distance(positions)

    print(f'Result for Part 1: {final_distance}')
    print(f'Result for Part 2: {max_distance}')
