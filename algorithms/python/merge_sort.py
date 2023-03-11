""" Merge Sort """
from typing import List


def merge(x: List[int], y: List[int]) -> List[int]:
    result = []

    i = 0
    j = 0
    while i < len(x) and j < len(y):
        if x[i] < y[j]:
            result.append(x[i])
            i += 1
        elif x[i] > y[j]:
            result.append(y[j])
            j += 1
        else:
            result.append(x[i])
            i += 1

    if i < len(x):
        result.extend(x[i:])
    elif j < len(y):
        result.extend(y[j:])

    return result


def merge_sort(x: List[int]):
    mid = (len(x) - 1) // 2

    while len(x) > 2:
        return merge(merge_sort(x[0 : mid + 1]), merge_sort(x[mid + 1 :]))

    if len(x) == 2:
        if x[0] < x[1]:
            return x
        else:
            x.reverse()
            return x

    return x


def main():
    x = [
        1,
        7,
        3,
        5,
        2,
        9,
        1,
        2,
        3,
        6,
        1,
        3,
        2,
        0,
        8,
        9,
        4,
        5,
        8,
        6,
        5,
        7,
        2,
        1,
        3,
        5,
        7,
        4,
    ]
    print(merge_sort(x))


if __name__ == "__main__":
    main()
