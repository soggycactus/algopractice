""" Merge Intervals """


def merge_arrays(smaller: list, bigger: list) -> list:
    """
    Merges two arrays if they overlap
    """
    if smaller[0] <= bigger[0] <= smaller[-1]:
        return [smaller[0], max(bigger[1], smaller[1])]


def merge(intervals: list) -> list:
    """
    Merges any overlapping intervals in the list and returns the result
    """
    if len(intervals) == 1:
        return intervals

    intervals.sort(key=lambda x: x[0])
    result = []
    current = intervals[0]
    i = 1
    while i < len(intervals):
        merged = merge_arrays(current, intervals[i])
        if merged is None:
            result.append(current)
            current = intervals[i]
        else:
            current = merged

        i += 1
    result.append(current)
    return result


def main():
    """
    Entrypoint
    """

    test_cases = [
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]],
        [[1, 4], [2, 5], [3, 7]],
        [[1, 3]],
        [[1, 4], [2, 3]],
        [[1, 4], [0, 2], [3, 5]],
        [[2, 3], [2, 2], [3, 3], [1, 3], [5, 7], [2, 2], [4, 6]],
        [
            [5, 5],
            [1, 3],
            [3, 5],
            [4, 6],
            [1, 1],
            [3, 3],
            [5, 6],
            [3, 3],
            [2, 4],
            [0, 0],
        ],
    ]

    for i in test_cases:
        print("original:", i)
        new = merge(i)
        print("new:", new)


if __name__ == "__main__":
    main()
