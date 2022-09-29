"""
Nicholas Yu
CSE 163 AD
This python file imports functions from hw1 python file
and runs them through functions that tests whether hw1
functions provide expected results.
"""

import hw1

from cse163_utils import assert_equals


def test_count_divisible_digits():
    """
    Tests count_divisible_digits and whether the funciton
    outputs expected and corret value. Includes a few other
    test cases apart from the given instructions.
    """
    assert_equals(4, hw1.count_divisible_digits(650899, 3))
    assert_equals(1, hw1.count_divisible_digits(-204, 5))
    assert_equals(0, hw1.count_divisible_digits(24, 55))
    assert_equals(0, hw1.count_divisible_digits(1, 0))
    assert_equals(0, hw1.count_divisible_digits(55, 55))
    assert_equals(3, hw1.count_divisible_digits(20321, 2))


def test_is_relatively_prime():
    """
    Tests is_relatively_prime and whether the funciton
    outputs expected and corret value. Includes a few other
    test cases apart from the given instructions.
    """
    assert_equals(True, hw1.is_relatively_prime(12, 13))
    assert_equals(False, hw1.is_relatively_prime(12, 14))
    assert_equals(True, hw1.is_relatively_prime(5, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 1))
    assert_equals(True, hw1.is_relatively_prime(1, 1))
    assert_equals(False, hw1.is_relatively_prime(27, 90))


def test_travel():
    """
    Tests travel function and whether the funciton
    outputs expected and corret tuple value. Includes a few other
    test cases apart from the given instructions.
    """
    assert_equals((-1, 4), hw1.travel('NW!ewnW', 1, 2))
    assert_equals((0, 0), hw1.travel('EWwSnE', 0, 0))
    assert_equals((9, 7), hw1.travel('E!e!e!E!E!W', 5, 7))
    assert_equals((-5, 0), hw1.travel('NWssEwS!', -4, 2))
    assert_equals((0, 0), hw1.travel('!!!!!!!', 0, 0))


def test_compress():
    """
    Tests compress function and whether the funciton
    outputs expected and corret string value. Includes a few other
    test cases apart from the given instructions.
    """
    assert_equals('c1o17l1k1a1n1g1a1r1o2', hw1.compress(
        'cooooooooooooooooolkangaroo'))
    assert_equals('a3', hw1.compress('aaa'))
    assert_equals('', hw1.compress(''))
    assert_equals('a5', hw1.compress('aaaaa'))
    assert_equals('h1e1l4o10w2h1a3', hw1.compress(
        'helllloooooooooowwhaaa'))


def test_get_average_in_range():
    """
    Tests get_average_in_range and whether the funciton
    outputs expected and corret average value. Includes a few other
    test cases apart from the given instructions.
    """
    assert_equals(5.5, hw1.get_average_in_range([1, 5, 6, 7, 9], 5, 7))
    assert_equals(2.0, hw1.get_average_in_range([1, 2, 3], -1, 10))
    assert_equals(6, hw1.get_average_in_range([3, 5, 7, 9], -1, 10))
    assert_equals(5.25, hw1.get_average_in_range([3, 4, 5, 9], 2, 10))
    assert_equals(0, hw1.get_average_in_range([3, 4, 5, 9], 11, 13))


def test_mode_digit():
    """
    Tests mode_digit and whether the funciton
    outputs expected and corret value. Includes a few other
    test cases apart from the given instructions.
    """
    assert_equals(1, hw1.mode_digit(12121))
    assert_equals(0, hw1.mode_digit(0))
    assert_equals(2, hw1.mode_digit(-122))
    assert_equals(2, hw1.mode_digit(1211232231))
    assert_equals(1, hw1.mode_digit(-121233010011))
    assert_equals(9, hw1.mode_digit(8977299189))


def test_longest_word():
    """
    Tests longest_word and whether the funciton
    outputs expected and information. Includes a few other
    test cases apart from the given instructions.
    """
    assert_equals('3: Merrily,', hw1.longest_word("/home/song.txt"))
    assert_equals('5: seasons', hw1.longest_word("/home/song2.txt"))
    assert_equals('7: demonstrating', hw1.longest_word("/home/song3.txt"))


def test_total():
    """
    Tests the total method
    """
    # The regular case
    assert_equals(15, hw1.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, hw1.total(1))
    assert_equals(0, hw1.total(0))

    # Test the None case
    assert_equals(None, hw1.total(-1))


def main():
    """
    Calls multiple test functions written above and
    run through each of them.
    """
    test_total()
    test_count_divisible_digits()
    test_is_relatively_prime()
    test_travel()
    test_compress()
    test_get_average_in_range()
    test_mode_digit()
    test_longest_word()


if __name__ == '__main__':
    main()
