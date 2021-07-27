""" Minimum Moves to Equal Array Elements """
from typing import List


def min_moves(nums: List[int]) -> int:
    """
    Returns the minimum number of moves to make all list elements equal
    """
    nums.sort()
    if len(nums) % 2 == 0:
        midpoint = (nums[(len(nums) // 2)] + nums[(len(nums) // 2) - 1]) // 2
    else:
        midpoint = nums[len(nums) // 2]

    moves = 0
    for number in nums:
        moves += abs(number - midpoint)

    return moves


def main():
    """
    Entrypoint
    """
    nums = [1, 10, 2, 9]
    print(min_moves(nums))


if __name__ == "__main__":
    main()
