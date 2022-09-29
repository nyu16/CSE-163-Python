"""
Nicholas Yu
CSE163 AD
The python file contains a number of functions that will be
executed as the given instructions. Though there's a number
of functions, the functions can be divided into one that deals
with data frame and actively utilizes the pandas library, while
the other half doesn't. However, each function is a duplicate
version of another.
"""


def total(n):
    """
    Returns the sum of the numbers from 0 to n (inclusive).
    If n is negative, returns None.
    """
    if n < 0:
        return None
    else:
        result = 0
        for i in range(n + 1):
            result += i
        return result


def count_divisible_digits(n, m):
    """
    Takes two integer numbers, n and m, as arguments and returns
    the number of digits that are within n and are divisible by m.
    If m is 0, then the function should return 0.
    """
    count = 0
    if m > 0:
        num = abs(n)
        while num > 0:
            if num % 10 == 0 or (num % 10) % m == 0:
                count += 1
            num //= 10
    if n == 0:
        return 1
    return count


def is_relatively_prime(n, m):
    """
    Takes two integer numbers n and m, and returns True if n and m are
    relatively prime to each other - if the two integers share no
    common factors besides 1. Otherwise False. 1 will be relatively
    prime with every number.
    """
    prime = n == 1 or m == 1
    if n > 1 and m > 1:
        prime = n != m
        for i in range(2, n):
            if n % i == 0 and m % i == 0:
                prime = False

    return prime


def travel(directions, x, y):
    """
    Takes a string of north, east, south, west directions, and
    the starting coordinates of x and y. The function returns a tuple
    of a new coordinate after following the given directions starting.
    """
    for i in directions:
        if i.upper() == 'N':
            y += 1
        elif i.upper() == 'E':
            x += 1
        elif i.upper() == 'S':
            y -= 1
        elif i.upper() == 'W':
            x -= 1

    return (x, y)


def compress(word):
    """
    Takes a string as an argument and returns a new string,
    and in it, each character is followed by its count. The
    function counts any adjacent duplicate characters and displays
    the the character and the number of its duplicates.
    """
    comp = ''
    count = 1
    for x in range(0, len(word)):
        if (x + 1) == len(word) or word[x] is not word[x+1]:
            comp += word[x] + str(count)
            count = 0
        count += 1

    return comp


def longest_word(filename):
    """
    Takes a file of string and returns the longest word in
    the file and its line number. If there are ties for the
    longest word, the function returns the one that appeared
    first. If the file is empty or there are no words in the file,
    the function returns None.
    """
    result = None

    with open(filename) as fn:
        longest = 0
        count = 1

        f = fn.readlines()
        for lines in f:
            words = lines.split()
            for word in words:
                if len(word) > longest:
                    longest = len(word)
                    result = str(count) + ": " + word
            count += 1

    return result


def get_average_in_range(nums, low, high):
    """
    Takes a list of integers, and integers low and high, and
    returns the average of all values within the list of digits
    that are in the range from low (inclusive) to high (exclusive).
    If there are no values in the given range, returns 0.
    """
    nums = [i for i in nums if i >= low and i < high]
    ave = 0
    if len(nums) != 0:
        for x in nums:
            ave += x
        ave /= len(nums)

    return ave


def mode_digit(n):
    """
    Takes an integer number n and returns the digit that appears
    most frequently in that number. The returning value will always
    be non-negative. If there is a tie for the most frequent digit,
    the digit with the greatest value is returned.
    """
    d = dict()
    num = abs(n)
    mode = 0
    longest = 0
    while num > 0:
        i = num % 10
        if i not in d:
            d[i] = 0
        d[i] += 1
        num //= 10

    for i in d.keys():
        if mode == 0 or mode <= d[i]:
            mode = d[i]
            longest = i

    return longest
