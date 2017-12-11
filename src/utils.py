import os.path
from functools import reduce
from typing import List, Iterable, Any, TypeVar, Tuple

T = TypeVar('T')


def get_file_path(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    parent_path = os.path.abspath(os.path.join(dir_path, os.pardir))
    return os.path.join(parent_path, 'data', file_name)


def read_first_line(file_name):
    file_path = get_file_path(file_name)

    with open(file_path) as f:
        return f.readline().strip()


def wrap_index(idx: int, xs: List):
    idx %= len(xs)
    return idx


def get_value_at_index(idx: int, xs: List[T]) -> T:
    return xs[wrap_index(idx, xs)]


def set_value_at_index(idx: int, value: Any, xs: List[T]) -> List[T]:
    xs[wrap_index(idx, xs)] = value
    return xs


def get_slice(xs: List, start: int, stop: int) -> List:
    return [get_value_at_index(idx, xs) for idx in range(start, stop)]


def set_slice(xs: List, subxs: Iterable, start: int, stop: int) -> List:
    xs = xs[:]
    for idx, value in enumerate(subxs, start):
        if idx >= stop:
            break
        set_value_at_index(idx, value, xs)
    return xs


def head(xs):
    if not xs:
        raise ValueError('head() on empty list.')
    return xs[0], xs[1:]


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


# Some typedef used through exercises
Step = Tuple[int, int]
Steps = List[Step]

Point = Tuple[int, int]
Points = List[Point]


def compute_coordinates_from_steps(start: Point, *steps: Steps) -> Point:
    """ Given a starting point and a sequence of cells, return the coordinate of the final point """

    def _sum(p1: Point, p2: Step) -> Point:
        x1, y1 = p1
        x2, y2 = p2
        return x1 + x2, y1 + y2

    return reduce(_sum, steps, start)
