"""
@author: Kush
Here we are given an array and are required to find the minimum sum of any three different elements in the array.
We will see both, a naive as well as an optimized implementation to solve this problem.
"""


def naive_solution(arr):
    """
    We use a triple loop to create all possible triplets and compute the
    minimum sum.
    """
    import sys, time

    start = time.time()
    min_sum = sys.maxsize
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            for k in range(j + 1, len(arr)):
                if arr[i] + arr[j] + arr[k] < min_sum:
                    min_sum = arr[i] + arr[j] + arr[k]

    return (min_sum, time.time() - start)


def optimized_solution(arr):
    """
    Here we will compute the sum by calulating the first, second and third minimum
    in the array. This approach will take O(n) time.
    """
    import sys, time

    start = time.time()
    min1 = sys.maxsize
    min2 = sys.maxsize
    min3 = sys.maxsize
    for i in range(len(arr)):
        if arr[i] < min1:
            min3 = min2
            min2 = min1
            min1 = arr[i]
        elif arr[i] < min2:
            min3 = min2
            min2 = arr[i]
        elif arr[i] < min3:
            min3 = arr[i]
    return ((min1 + min2 + min3), time.time() - start)


if __name__ == "__main__":
    from random import randint

    arr = [random.randint(-1000, 1000) for i in range(500)]
    ans1 = naive_solution(arr)
    ans2 = optimized_solution(arr)
    print(f"The minimum sum is {ans1[0]} computed in time {ans1[1]} seconds.")
    print(f"The minimum sum is {ans2[0]} computed in time {ans2[1]} seconds.")
