"""
A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password.
A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.
The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

For added security, yet another system policy has been put in place.
Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid
if any word's letters can be rearranged to form any other word in the passphrase.
"""
from src.utils import get_file_path


def is_passphrase_valid(passphrase):
    words = passphrase.split()
    return len(set(words)) == len(words)


def is_passphrase_valid_anagrams(passphrase):
    words = passphrase.split()
    return contain_anagrams(words) is False


def contain_anagrams(words):
    sorted_words = [''.join(sorted(w)) for w in words]
    return len(set(sorted_words)) != len(sorted_words)


if __name__ == '__main__':
    input_file_path = get_file_path('passphrases.txt')

    with open(input_file_path) as f:
        passphrases = [line.strip() for line in f.readlines()]

    valid_passphrases = sum(1 for passphrase in passphrases if is_passphrase_valid(passphrase))

    print(f'Result for Part 1: {valid_passphrases}')

    valid_passphrases = sum(1 for passphrase in passphrases if is_passphrase_valid_anagrams(passphrase))

    print(f'Result for Part 2: {valid_passphrases}')

