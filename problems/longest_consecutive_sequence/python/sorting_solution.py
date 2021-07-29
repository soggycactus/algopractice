""" Longest Consecutive Sequence """
from typing import List


def longest_consecutive(nums: List[int]) -> int:
    """
    Returns the longest consecutive sequence of a list
    """
    if nums == []:
        return 0
    nums = list(set(nums))
    nums.sort()
    sequence = 1
    current = 1
    for i in range(1, len(nums)):
        if nums[i] - 1 == nums[i - 1]:
            current += 1
        else:
            if current > sequence:
                sequence = current
            current = 1
    if current > sequence:
        return current
    return sequence


def main():
    """
    Entrypoint
    """
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(longest_consecutive(nums))


if __name__ == "__main__":
    main()
