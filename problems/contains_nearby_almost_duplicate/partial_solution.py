""" Contains Nearby Almost Duplicate """
from itertools import combinations


def contains_nearby_almost_duplicate(nums: list, k: int, t: int) -> bool:
    """
    Returns True if nums contains nearby almost duplicate
    """
    to_check = list(combinations(range(0, len(nums)), 2))
    for i, j in to_check:
        if abs(i - j) > k:
            continue
        if abs(nums[i] - nums[j]) > t:
            continue
        return True

    return False


def main():
    """
    Entrypoint
    """
    nums = [1, 5, 9, 1, 5, 9]
    k = 2
    t = 3

    print(contains_nearby_almost_duplicate(nums, k, t))


if __name__ == "__main__":
    main()
