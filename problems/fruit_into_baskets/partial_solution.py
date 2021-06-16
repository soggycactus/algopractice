""" Fruit into Baskets """


def find_longest_subarray_of_two_values(array: list, start=0):
    """
    Finds the longest subarray consisting of only 2 values in an array
    """
    if len(array[start:]) == 1:
        return [start, start]
    if len(array[start:]) == 0:
        return array

    a = array[start]
    b = None
    end = None

    for i in range(start + 1, len(array)):
        if array[i] != a:
            b = array[i]
            end = i - 1
            break

    if end is None:
        return [start, len(array) - 1]

    found_end = False
    for i in range(end + 1, len(array)):
        if array[i] != a and array[i] != b:
            end = i - 1
            found_end = True
            break

    if found_end is False:
        return [start, len(array) - 1]

    next_subarray = find_longest_subarray_of_two_values(array, start + 1)
    if len(array[next_subarray[0] : next_subarray[1] + 1]) > len(
        array[start : end + 1]
    ):
        return next_subarray

    return [start, end]


def main():
    """
    Entrypoint
    """
    test_cases = [
        [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4],
        [1, 2, 1],
        [0, 1, 2, 2],
        [1, 2, 3, 2, 2],
        [0, 0, 1, 1],
        [0, 1, 6, 6, 4, 4, 6],
    ]
    for test in test_cases:
        i, j = find_longest_subarray_of_two_values(test)
        print("test case:", test)
        print(test[i : j + 1])
        print(len(test[i : j + 1]))


if __name__ == "__main__":
    main()
