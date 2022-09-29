"""
Nicolas Yu
Section AD
Implements the functions for HW0
"""
import hw0

from cse163_utils import assert_equals


def test_total():
    """
    calls the function assert_equal in order to check if the called function,
    which in this case is hw0.total, produces the expected value. Returns
    nothing.
    """
    # The regular case
    assert_equals(15, hw0.total(5))
    # Seems likely we could mess up 0 or 1
    assert_equals(1, hw0.total(1))
    assert_equals(0, hw0.total(0))
    assert_equals(55, hw0.total(10))
    assert_equals(276, hw0.total(23))
    assert_equals(None, hw0.total(-10))
    assert_equals(None, hw0.total(-3))


def test_funky_sum():
    """
    calls in assert_equal to test whether funky_sum produces the expected
    output by passing parameters of expected value and the testing function
    into assert_equals. If the result fails then error message will show
    telling us False is not True
    """
    assert_equals(2.0, hw0.funky_sum(1, 3, 0.5))
    assert_equals(1.0, hw0.funky_sum(1, 3, 0))
    assert_equals(2.0, hw0.funky_sum(2, 4, -1))
    assert_equals(5.0, hw0.funky_sum(9, 5, 10))
    assert_equals(3.0, hw0.funky_sum(1, 3, 1))
    assert_equals(2.6, hw0.funky_sum(2, 8, 0.1))


def test_swip_swap():
    """
    calls in assert_equal to test whether swimp_swap produces the expected
    output by passing parameters of expected value and the testing function
    into assert_equals. If the result fails then error message will show
    telling us False is not True
    """
    assert_equals('offbar', hw0.swip_swap('foobar', 'f', 'o'))
    assert_equals('foocar', hw0.swip_swap('foobar', 'b', 'c'))
    assert_equals('foobar', hw0.swip_swap('foobar', 'z', 'c'))
    assert_equals('ylollllw', hw0.swip_swap('yoloooow', 'o', 'l'))
    assert_equals('ehytehrh', hw0.swip_swap('heythere', 'e', 'h'))


def main():
    """
    main function calling test_total(). Returns nothing and takes in nothing
    as a parameter
    """
    test_total()
    test_funky_sum()
    test_swip_swap()


if __name__ == '__main__':
    main()
