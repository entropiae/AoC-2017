from src.utils import wrap_index


def test_wrap_index():
    xs = [1, 2, 3, 4, 5]
    idx = 26

    normalized_idx = wrap_index(idx, xs)
    expected_normalized_idx = 1
    assert normalized_idx == expected_normalized_idx
