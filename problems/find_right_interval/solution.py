""" Find Right Interval """


def binary_search(array: list, target: int, key=lambda x: x):
    """
    implements binary search
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = left + ((right - left) // 2)
        value = key(array[mid])

        if target == value:
            return mid
        elif target < value:
            right = mid - 1
        else:
            left = mid + 1


def find_right_interval(intervals: list) -> list:
    max_start = max(intervals, key=lambda x: x[0])[0]
    to_search = [(intervals[x], x) for x in range(0, len(intervals))]
    to_search.sort(key=lambda x: x[0][0])
    result = []

    for i in intervals:
        appended = False
        end = i[1]

        while end <= max_start:
            start = binary_search(to_search, end, lambda x: x[0][0])
            if start is not None:
                result.append(to_search[start][1])
                appended = True
                break
            else:
                end += 1

        if appended is True:
            continue
        else:
            result.append(-1)

    return result


def main():
    """
    Entrypoint
    """
    test_cases = [
        [[1, 2]],
        [[3, 4], [2, 3], [1, 2]],
        [[1, 4], [2, 3], [3, 4]],
    ]

    for i in test_cases:
        print(find_right_interval(i))


if __name__ == "__main__":
    main()
