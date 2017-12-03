from src.aoc_3_spiral_memory import compute_distance, generate_sum_distance


def test_distance_1():
    """Data from square 1 is carried 0 steps, since it's at the access port."""
    cell_address = 1
    expected_distance = 0

    distance = compute_distance(cell_address)
    assert distance == expected_distance


def test_distance_2():
    """Data from square 12 is carried 3 steps, such as: down, left, left."""
    cell_address = 12
    expected_distance = 3

    distance = compute_distance(cell_address)
    assert distance == expected_distance


def test_distance_3():
    """Data from square 23 is carried only 2 steps: up twice."""
    cell_address = 23
    expected_distance = 2

    distance = compute_distance(cell_address)
    assert distance == expected_distance


def test_distance_4():
    """Data from square 1024 must be carried 31 steps."""
    cell_address = 1024
    expected_distance = 31

    distance = compute_distance(cell_address)
    assert distance == expected_distance


def test_sum_distance():
    """
    Square 1 starts with the value 1.
    Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
    Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
    Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
    Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
    :return:
    """
    sum_distance = generate_sum_distance()
    first_5_values = dict((idx, next(sum_distance)[1]) for idx in range(1, 6))

    assert first_5_values[1] == 1
    assert first_5_values[2] == 1
    assert first_5_values[3] == 2
    assert first_5_values[4] == 4
    assert first_5_values[5] == 5

