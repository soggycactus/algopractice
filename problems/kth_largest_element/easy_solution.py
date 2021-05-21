""" The easy solution to kth largest element """


def find_kth_largest(nums: list, k: int) -> int:
    """
    Returns the kth largest element in an array
    """
    nums = sorted(nums)
    nums.reverse()
    return nums[k - 1]


def main():
    """
    Entrypoint
    """
    array = [1, 2, 7, 4, 8, 9, 12, 3, 23, 3, 4]
    print(sorted(array))
    print(find_kth_largest(array, 3))


if __name__ == "__main__":
    main()
