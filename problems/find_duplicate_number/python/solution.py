""" Find Duplicate Number """


def find_duplicate(nums: list) -> int:
    """
    Finds the first duplicate value in a list of integers
    """
    hash_table = dict()
    for i in nums:
        if hash_table.get(i) is None:
            hash_table[i] = 1
        else:
            return i

    return -1


def main():
    """
    Entrypoint
    """
    nums = [1, 3, 4, 2, 2]
    print(find_duplicate(nums))


if __name__ == "__main__":
    main()
