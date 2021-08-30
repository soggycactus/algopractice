""" Range Addition """
from typing import List


def max_count(m: int, n: int, ops: List[List[int]]) -> int:
    """
    Returns the number of maximum integers after all operations have been performed
    """
    if ops == []:
        return m * n

    row = m * n + 1
    column = m * n + 1
    for r, c in ops:
        if r < row:
            row = r
        if c < column:
            column = c

    return row * column


def main():
    """
    Entrypoint
    """
    m = 3
    n = 3
    ops = [[2, 2], [3, 3]]
    print(max_count(m, n, ops))


if __name__ == "__main__":
    main()
