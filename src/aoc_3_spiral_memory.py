from itertools import count

from functools import reduce

"""
You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1
and then counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1
(the location of the only access port for this memory system) by programs that can only move up, down, left, or right.
They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

How many steps are required to carry the data from the square identified in your puzzle input all the way to the
access port?
"""

BASE_COORDINATES = (0, 0)


def compute_distance(cell_address):
    """
    Return the Manhattan Distance of the cell with a given address from the (0, 0) cell.
    """
    address = generate_step()
    steps = [next(address) for _ in range(2, cell_address + 1)]
    cell_coordinates = compute_coordinates_from_steps(BASE_COORDINATES, *steps)
    print(f'Coordinates for call with address {cell_address}: {cell_coordinates}')
    return manhattan_distance((0, 0), cell_coordinates)


def generate_sum_distance():
    """ Generate a sequence of (coordinate, value) starting from BASE_COORDINATES """
    adjacent_values = {BASE_COORDINATES: 1}
    coordinates = BASE_COORDINATES

    yield BASE_COORDINATES, 1

    for step in generate_step():
        coordinates = compute_coordinates_from_steps(coordinates, step)

        sum_adjacent_values = sum(get_adjacent_values(coordinates, adjacent_values))
        yield coordinates, sum_adjacent_values
        adjacent_values[coordinates] = sum_adjacent_values


def get_adjacent_values(coordinate, adjacent_values):
    """
    Generate the sequence of values contained in the adjacent cells.
    Coordinates of the current cell must not be in adjacent_values, otherwise its
    value will be returned as well.
    """
    x, y = coordinate
    for x_adj in (-1, 0, 1):
        for y_adj in (-1, 0, 1):
            yield adjacent_values.get((x + x_adj, y + y_adj), 0)


def generate_step():
    """ Generate the sequence of step used to address our matrix cells."""
    for index in count():
        step = 1 if index % 2 else -1
        for _ in range(index):
            yield step, 0
        for _ in range(index):
            yield 0, step


def compute_coordinates_from_steps(start, *steps):
    """ Given a starting point and a sequence of cells, return the coordinate of the final point """
    def _sum(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return x1 + x2, y1 + y2

    return reduce(_sum, steps, start)


def manhattan_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


if __name__ == '__main__':
    puzzle_input = 265149
    result = compute_distance(puzzle_input)
    print(f'Result for Part 1: {result}')

    distance_gen = generate_sum_distance()
    result = 0
    while result <= puzzle_input:
        _, result = next(distance_gen)

    print(f'Result for Part 2: {result}')
