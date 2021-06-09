""" Search Insert Position """


def search_insert(nums: list, target: int) -> int:
    """
    Returns the index of the target if found, or where it would be inserted if not found
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + ((right - left) // 2)

        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return mid if target < nums[mid] else mid + 1


def main():
    """
    Entrypoint
    """
    nums = [1, 3, 5, 6]
    print(search_insert(nums, 5))
    print(search_insert(nums, 2))
    print(search_insert(nums, 7))
    print(search_insert(nums, 0))

    nums = [1]
    print(search_insert(nums, 0))

    nums = [1, 3]
    print(search_insert(nums, 0))


if __name__ == "__main__":
    main()
