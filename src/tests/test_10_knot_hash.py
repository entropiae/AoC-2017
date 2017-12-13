from src.aoc_10_knot_hash import hash_round, step, parse_keys_part_2, knot_hash


def test_part_1():
    input_list = [0, 1, 2, 3, 4]
    input_keys = [3, 4, 1, 5]

    expected_output = [3, 4, 2, 1, 0]
    output = hash_round(input_list, input_keys)
    assert output == expected_output


def test_hash_step():
    plain = [0, 1, 2, 3, 4]
    position = 0
    skip_size = 0
    key = 3

    plain, position, skip_size = step(plain, position, skip_size, key)
    assert plain == [2, 1, 0, 3, 4]
    assert position == 3
    assert skip_size == 1

    key = 4
    plain, position, skip_size = step(plain, position, skip_size, key)
    assert plain == [4, 3, 0, 1, 2]
    assert position == 3
    assert skip_size == 2


def test_parse_keys_part_2():
    raw_keys = '1,2,3'
    parsed_keys = [49, 44, 50, 44, 51, 17, 31, 73, 47, 23]

    keys = parse_keys_part_2(raw_keys)
    assert keys == parsed_keys


def test_knot_hash():
    plain = list(range(256))
    assert knot_hash(plain, parse_keys_part_2('')) == 'a2582a3a0e66e6e86e3812dcb672a272'
    assert knot_hash(plain, parse_keys_part_2('AoC 2017')) == '33efeb34ea91902bb2f59c9920caa6cd'
    assert knot_hash(plain, parse_keys_part_2('1,2,3')) == '3efbe78a8d82f29979031a4aa0b16a9d'
    assert knot_hash(plain, parse_keys_part_2('1,2,4')) == '63960835bcdc130f0b66d7ff4f6a5a8e'
