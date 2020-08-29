"""
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence
1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention,
1 is included.
Given an integer n, we have to find the nth ugly number
"""
"""
As always, we will look at two different approaches to solevthis problem.
First is the naive approach where we just loop on numbers untill we have the nth ugly number.
"""

def max_divide(a: int, b: int) -> int:
    """
    Returns a after dividing it with the greatest possible power of b.
    >>> max_divide(729,3)
    1
    >>> max_divide(7543,2)
    7543
    >>> max_divide(486,3)
    2
    """
    while a % b == 0:
        a //= b
    return a


def is_ugly(n: int) -> bool:
    """
    Returns True if n is ugly, False otherwise.
    >>> is_ugly(12)
    True
    >>> is_ugly(14)
    False
    >>> is_ugly(120)
    True
    """
    n = max_divide(n, 2)
    n = max_divide(n, 3)
    n = max_divide(n, 5)
    return n == 1


def naive_solution(n: int) -> int:
    """
    Returns the nth ugly number.
    >>> naive_solution(100)
    1536
    >>> naive_solution(1)
    1
    >>> naive_solution(20)
    36
    """
    count = 1
    num = 1
    while count < n:
        num += 1
        if is_ugly(num):
            count += 1
    return num
"""
Now we will see a different approach which uses the dynamic programming technique to solve the same problem.
For detailed explanation, check this article:
https://www.geeksforgeeks.org/ugly-numbers/
"""

def ugly_numbers(n: int) -> int:
    """
    Uses dynamic programming technique to return the nth ugly number.
    >>> ugly_numbers(100)
    1536
    >>> ugly_numbers(1)
    1
    >>> ugly_numbers(20)
    36
    """
    ugly_nums = [0] * (n)
    ugly_nums[0] = 1

    i2, i3, i5 = 0, 0, 0
    next_2 = ugly_nums[i2] * 2
    next_3 = ugly_nums[i3] * 3
    next_5 = ugly_nums[i5] * 5

    for i in range(1, n):
        next_num = min(next_2, next_3, next_5)
        ugly_nums[i] = next_num
        if next_num == next_2:
            i2 += 1
            next_2 = ugly_nums[i2] * 2
        if next_num == next_3:
            i3 += 1
            next_3 = ugly_nums[i3] * 3
        if next_num == next_5:
            i5 += 1
            next_5 = ugly_nums[i5] * 5
    return ugly_nums[-1]


if __name__ == "__main__":
    from doctest import testmod

    testmod()
    print(f"{naive_solution(150)}")
    print(f"{ugly_numbers(150)}")
