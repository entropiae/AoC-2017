import os.path


def get_file_path(file_name):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    parent_path = os.path.abspath(os.path.join(dir_path, os.pardir))
    return os.path.join(parent_path, 'data', file_name)
