""" Find Peak Elements - two pointer solution"""


def find_peak_elements(nums: list) -> int:
    """
    Returns a peak element from nums
    """
    if len(nums) == 1:
        return 0

    i = 0
    j = len(nums) - 1

    if nums[i] > nums[i + 1]:
        return i

    if nums[j] > nums[j - 1]:
        return j

    i += 1
    j -= 1

    while i != j:
        if nums[i - 1] < nums[i] > nums[i + 1]:
            return i
        elif nums[j - 1] < nums[j] > nums[j + 1]:
            return j
        else:
            i += 1
            j -= 1

    return i


def main():
    """
    Entrypoint
    """
    test_cases = [
        [1, 2, 3, 1],
        [1, 2, 1, 3, 5, 6, 4],
    ]
    for test in test_cases:
        print(find_peak_elements(test))


if __name__ == "__main__":
    main()
