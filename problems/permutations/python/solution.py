""" Permutations """
from typing import List


def permutations(array: List[int]) -> List[List[int]]:
    """
    Returns all the possible permutations of the provided array
    """
    if len(array) == 1:
        return [array]
    if len(array) == 2:
        return [[array[0], array[1]], [array[1], array[0]]]

    result = []
    for i in range(0, len(array)):
        subarrays = permutations(array[0:i] + array[i + 1 :])
        for j in subarrays:
            result.append([array[i]] + j)

    return result


def main():
    """
    Entrypoint
    """
    array = [1, 2, 3, 4, 5, 6]
    print(permutations(array))


if __name__ == "__main__":
    main()
