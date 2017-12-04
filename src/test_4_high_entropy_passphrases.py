from src.aoc_4_high_entropy_passphrases import is_passphrase_valid, is_passphrase_valid_anagrams


def test_passphrase_check():
    assert is_passphrase_valid('aa bb cc dd ee')
    assert is_passphrase_valid('aa bb cc dd aa') is False
    assert is_passphrase_valid('aa bb cc dd aaa')


def test_anagrams_passphrases():
    assert is_passphrase_valid_anagrams('abcde fghij')
    assert is_passphrase_valid_anagrams('abcde xyz ecdab') is False
    assert is_passphrase_valid_anagrams('a ab abc abd abf abj')
    assert is_passphrase_valid_anagrams('iiii oiii ooii oooi oooo')
    assert is_passphrase_valid_anagrams('oiii ioii iioi iiio') is False
