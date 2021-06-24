""" First Missing Positive """


def first_missing_positive(nums: list) -> int:
    """
    Returns the first missing positive number in an unsorted sequence of numbers
    """
    hash_table = dict()

    for i in nums:
        hash_table[i] = True

    j = 1
    while j <= len(nums):
        if hash_table.get(j) is not None:
            j += 1
        else:
            return j

    return j


def main():
    """
    Entrypoint
    """

    test_cases = [
        [1, 2, 0],
        [3, 4, -1, 1],
        [7, 8, 9, 11, 12],
        [2],
        [1],
    ]

    for test in test_cases:
        print(first_missing_positive(test))


if __name__ == "__main__":
    main()
