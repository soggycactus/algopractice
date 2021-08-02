""" Find Minimum in Rotated Sorted Array """

from typing import List


def find_min(nums: List[int]) -> int:
    """
    Finds the minimum number in a rotated sorted array
    """
    if len(nums) == 1:
        return nums[0]

    left = 0
    right = len(nums) - 1

    if nums[right] > nums[left]:
        return nums[left]

    while left <= right:
        mid = left + ((right - left) // 2)

        if nums[mid - 1] > nums[mid] < nums[mid + 1]:
            return nums[mid]
        elif nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        elif nums[mid] > nums[left]:
            left = mid + 1
        else:
            right = mid - 1


def main():
    """
    Entrypoint
    """
    nums = [3, 4, 5, 1, 2]
    print(find_min(nums))


if __name__ == "__main__":
    main()
