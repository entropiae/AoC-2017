import pytest

from src.utils import wrap_index, head, get_slice, set_slice


def test_wrap_index():
    xs = [1, 2, 3, 4, 5]
    idx = 26

    normalized_idx = wrap_index(idx, xs)
    expected_normalized_idx = 1
    assert normalized_idx == expected_normalized_idx


def test_head():
    xs = [1, 2, 3, 4]
    h, t = head(xs)

    assert h == 1
    assert t == [2, 3, 4]


def test_head_one_item():
    xs = [1]
    h, t = head(xs)

    assert h == 1
    assert t == []


def test_head_empty_raise():
    with pytest.raises(ValueError):
        head([])


def test_sublist():
    xs = [0, 1, 2, 3, 4]
    start, stop = 3, 5
    expected_output = [3, 4]
    output = get_slice(xs, start, stop)
    assert output == expected_output


def test_sublist_wrap():
    xs = [0, 1, 2, 3, 4]
    start, stop = 3, 7
    expected_output = [3, 4, 0, 1]
    output = get_slice(xs, start, stop)
    assert output == expected_output


def test_sublist_set():
    xs = [0, 1, 2, 3, 4]
    subxs = [5, 6]
    start, stop = 0, 2

    output = set_slice(xs, subxs, start, stop)
    assert output == [5, 6, 2, 3, 4]


def test_sublist_set_wrap():
    xs = [0, 1, 2, 3, 4]
    subxs = [5, 6]
    start, stop = 5, 7

    output = set_slice(xs, subxs, start, stop)
    assert output == [5, 6, 2, 3, 4]
