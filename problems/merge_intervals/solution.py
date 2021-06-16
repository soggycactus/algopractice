""" Merge Intervals """


def merge(intervals: list) -> list:
    """
    Merges any overlapping intervals in the list and returns the result
    """
    if len(intervals) == 1:
        return intervals

    intervals.sort(key=lambda x: x[0])

    result = []

    while intervals != []:
        if len(intervals) == 1:
            result.extend(intervals)
            break

        for i in range(1, len(intervals)):
            if intervals[0][0] <= intervals[i][0] <= intervals[0][1]:
                intervals.append(
                    [intervals[0][0], max(intervals[i][1], intervals[0][1])]
                )
                del intervals[0 : i + 1]
                intervals.sort(key=lambda x: x[0])
                break
            elif i == len(intervals) - 1:
                result.append(intervals[0])
                del intervals[0]
                break
            else:
                continue

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
