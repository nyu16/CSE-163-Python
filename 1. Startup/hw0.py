"""
Nicolas Yu
Section AD
Implements the functions for HW0
"""


def funky_sum(a, b, mix):
    """
    Take 3 parameters, the first two being integers a and b
    to combine and a third that'll determine the ratio of usage
    for each integer. Mix acts as a "slider" to control how much
    of each integers a and b will be used. If mix is 0 or less,
    a is returned. If mix is 1 or more, the b is returned. For any value
    of mix between 0 and 1, the functions returns a value that adds mix
    subtracted from 1 multiplied by a, and mix multiplied by b.
    """
    if mix <= 0:
        return a
    elif mix >= 1:
        return b
    else:
        return (1 - mix) * a + mix * b


def total(n):
    """
    takes in an integer n
    sums numbers from 0 to n inclusive and returns the value
    if n is negative the function returns None
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


def swip_swap(source, c1, c2):
    """
    takes in a string and two characters of c1 and c2 as parameters, swaps
    c1 and c2 within the string and returns a new string in which all c1s
    are swapped to c2 and all c2s are swithced to c1s
    """
    new_str = ''
    for i in source:
        if i == c1:
            new_str += c2
        elif i == c2:
            new_str += c1
        else:
            new_str += i
    return new_str
