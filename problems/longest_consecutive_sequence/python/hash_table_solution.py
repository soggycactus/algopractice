""" Longest Consecutive Sequence """
from typing import List


def longest_consecutive(nums: List[int]) -> int:
    """
    Returns the longest consecutive sequence of a list
    """
    longest_streak = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


def main():
    """
    Entrypoint
    """
    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(longest_consecutive(nums))


if __name__ == "__main__":
    main()
