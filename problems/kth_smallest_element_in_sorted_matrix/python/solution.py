""" Kth Smallest Element in Sorted Matrix """

from typing import List


def flatten(array: List[List[int]]):
    """
    Flattens a matrix
    """
    result = []
    for i in array:
        result.extend(i)

    return result


def kth_smallest(matrix: List[List[int]], k: int) -> int:
    """
    Returns Kth smallest element of sorted matrix
    """
    matrix = flatten(matrix)
    matrix.sort()
    return matrix[k - 1]


def main():
    """
    Entrypoint
    """
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    print(kth_smallest(matrix, k))


if __name__ == "__main__":
    main()
