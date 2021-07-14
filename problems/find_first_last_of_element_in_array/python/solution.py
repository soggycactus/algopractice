""" First and Last Element in Sorted Array """


def search_range(nums: list, target: int) -> list:
    """
    Returns starting & ending index of the target in a sorted array, [-1,-1] if it's non-existent
    """
    if nums == []:
        return [-1, -1]

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + ((right - left) // 2)

        if target == nums[mid]:
            start = mid
            end = mid

            while start >= 0:
                if nums[start] != target:
                    break
                start -= 1

            while end <= len(nums) - 1:
                if nums[end] != target:
                    break
                end += 1

            return [start + 1, end - 1]
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return [-1, -1]


def main():
    """
    Entrypoint
    """
    nums = [5, 7, 7, 8, 8, 10]
    print(search_range(nums, 10))
    print(search_range(nums, 8))
    print(search_range(nums, 6))


if __name__ == "__main__":
    main()
