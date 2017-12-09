import os.path


def get_file_path(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    parent_path = os.path.abspath(os.path.join(dir_path, os.pardir))
    return os.path.join(parent_path, 'data', file_name)


def wrap_index(idx, xs):
    idx %= len(xs)
    return idx


def get_element_in_position(idx, xs):
    return xs[wrap_index(idx, xs)]


def head(xs):
    if not xs:
        raise ValueError('head() on empty list.')
    return xs[0], xs[1:]
