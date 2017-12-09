import pytest

from src.utils import wrap_index, head


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
