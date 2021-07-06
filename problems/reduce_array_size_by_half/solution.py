""" Reduce Array Size by Half """

from heapq import heapify, heappop


def min_set_size(arr: list) -> int:
    """
    Returns the minimum number of elements that should be removed from the array
    to reduce its size by at least half
    """
    hash_table = dict()
    for i in arr:
        if hash_table.get(i) is None:
            hash_table[i] = -1
        else:
            hash_table[i] -= 1

    hash_table = list(hash_table.values())
    heapify(hash_table)

    result = 0
    count = 0
    target = len(arr) // 2

    while result < target:
        result += -heappop(hash_table)
        count += 1

    return count


def main():
    """
    Entrypoint
    """
    test_cases = [
        [3, 3, 3, 3, 5, 5, 5, 2, 2, 7],
        [7, 7, 7, 7, 7, 7],
        [1, 9],
        [1000, 1000, 3, 7],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ]

    for test in test_cases:
        print(min_set_size(test))


if __name__ == "__main__":
    main()
