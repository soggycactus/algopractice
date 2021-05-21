""" Kth Smallest Distance Pair """
from heapq import heapify, heappop
from itertools import combinations


def kth_smallest_distance_pair(array: list, k: int) -> int:
    """
    Returns the kth smallest distance pair
    """
    distance_pairs = []
    pairs = list(combinations(array, 2))

    for i, j in pairs:
        distance_pairs.append(abs(i - j))

    heapify(distance_pairs)

    for _ in range(0, k):
        value = heappop(distance_pairs)

    return value


def main():
    """
    Entrypoint of the program
    """
    array = [62, 100, 4]
    k = 2

    print(array)
    print(kth_smallest_distance_pair(array, k))


if __name__ == "__main__":
    main()
