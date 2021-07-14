""" Heap solution to kth largest element """
from heapq import heapify, heappop


def find_kth_largest(array: list, k: int) -> int:
    """
    Returns kth largest element in array
    """
    array = [-x for x in array]
    heapify(array)

    for _ in range(0, k):
        value = heappop(array)

    return -value


def main():
    """
    Entrypoint to program
    """
    array = [1, 2, 7, 4, 8, 9, 12, 3, 23, 3, 4]
    heapify(array)

    k = 3
    print(sorted(array))
    print(find_kth_largest(array, k))


if __name__ == "__main__":
    main()
