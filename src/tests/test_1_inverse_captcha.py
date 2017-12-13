from src.aoc_1_inverse_captcha import inverse_captcha_next, inverse_captcha_halfway


def test_next_1():
    """
    1122 produces a sum of 3 (1 + 2) because the first digit (1)
    matches the second digit and the third digit (2) matches the fourth digit.
    """
    assert inverse_captcha_next('1122') == 3


def test_next_2():
    """1111 produces 4 because each digit (all 1) matches the next."""
    assert inverse_captcha_next('1111') == 4


def test_next_3():
    """1234 produces 0 because no digit matches the next."""
    assert inverse_captcha_next('1234') == 0


def test_next_4():
    """91212129 produces 9 because the only digit that matches the next one is the last digit, 9."""
    assert inverse_captcha_next('91212129') == 9


def test_halfway_1():
    """1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead."""
    assert inverse_captcha_halfway('1212') == 6


def test_halfway_2():
    """1221 produces 0, because every comparison is between a 1 and a 2."""
    assert inverse_captcha_halfway('1221') == 0


def test_halfway_3():
    """123425 produces 4, because both 2s match each other, but no other digit has a match."""
    assert inverse_captcha_halfway('123425') == 4


def test_halfway_4():
    """123123 produces 12."""
    assert inverse_captcha_halfway('123123') == 12


def test_halfway_5():
    """12131415 produces 4."""
    assert inverse_captcha_halfway('12131415') == 4