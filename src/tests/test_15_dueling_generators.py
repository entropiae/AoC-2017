from src.aoc_15_dueling_generators import generator, judge


def test_part_1():
    a = generator(65, 16807)
    b = generator(8921, 48271)

    equal_count = judge(a, b, sample_size=5)
    assert equal_count == 1


def test_part_2():
    a = generator(65, 16807, 4)
    b = generator(8921, 48271, 8)

    equal_count = judge(a, b, sample_size=1056)
    assert equal_count == 1
