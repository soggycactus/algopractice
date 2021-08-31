""" Missing Element in Sorted Array """
from typing import List


def missing_element(nums: List[int], k: int) -> int:
    """
    Returns the kth missing element from nums
    """
    left = 0
    right = 1

    remaining = k

    while right < len(nums):
        available = (nums[right] - nums[left]) - 1
        if available == -1:
            left += 1
            right += 1
        elif available < remaining:
            remaining -= available
            left += 1
            right += 1
        else:
            return nums[left] + remaining

    return nums[-1] + remaining


def main():
    """
    Entrypoint
    """
    nums = [4, 7, 9, 10]
    k = 4
    print(missing_element(nums, k))


if __name__ == "__main__":
    main()
