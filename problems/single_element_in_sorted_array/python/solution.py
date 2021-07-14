""" Single Element in Sorted Array """


def find_unique(nums: list, left: int, right: int) -> int:
    """
    Finds the unique element in a sorted array of integers
    """
    if len(nums) == 1:
        return nums[0]

    while left <= right:
        mid = left + ((right - left) // 2)

        if mid == len(nums) - 1:
            return nums[mid] if nums[mid] != nums[mid - 1] else None
        elif mid == 0:
            return nums[mid] if nums[mid] != nums[mid + 1] else None
        elif nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
            return nums[mid]
        else:
            new_right = mid - 1
            new_left = mid + 1
            left_result = find_unique(nums, left, new_right)

            if left_result is None:
                return find_unique(nums, new_left, len(nums) - 1)

            return left_result

    return None


def main():
    """
    Entrypoint
    """
    test_cases = [
        [1, 1, 2, 3, 3, 4, 4, 8, 8],
        [3, 3, 7, 7, 10, 11, 11],
        [1, 1, 2, 2, 3],
    ]

    for i in test_cases:
        print(find_unique(i, 0, len(i) - 1))


if __name__ == "__main__":
    main()
