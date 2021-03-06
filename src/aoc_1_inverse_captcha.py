from src.utils import get_value_at_index, read_first_line


def inverse_captcha_next(in_str):
    """
    The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all digits that
    match the next digit in the list.
    The list is circular, so the digit after the last digit is the first digit in the list.

    What is the solution to your captcha?
    """
    def get_reference_char(idx):
        return get_value_at_index(idx + 1, in_str)

    return _inverse_captcha(in_str, get_reference_char)


def inverse_captcha_halfway(in_str):
    """
    Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list.
    That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 s
    teps forward matches it. Fortunately, your list has an even number of elements.

    What is the solution to your new captcha?
    """
    def get_reference_char(idx):
        return get_value_at_index(idx + int(len(in_str) / 2), in_str)

    return _inverse_captcha(in_str, get_reference_char)


def _inverse_captcha(in_str, get_ref_char):
    return sum(int(c) for idx, c in enumerate(in_str) if c == get_ref_char(idx))


if __name__ == '__main__':
    puzzle_input = read_first_line('inverse_captcha.txt')

    next_result = inverse_captcha_next(puzzle_input)
    print(f'Result for Part 1: {next_result}')
    halfway_result = inverse_captcha_halfway(puzzle_input)
    print(f'Result for Part 2: {halfway_result}')
