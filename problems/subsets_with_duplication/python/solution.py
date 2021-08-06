""" Subsets with Duplication """
from typing import List


def subsets_with_dup(nums: List[int], memo: dict) -> List[List[int]]:
    """
    Returns all possible subsets of nums
    """
    hash_code = hash(str(sorted(nums)))
    if memo.get(hash_code) is not None:
        return memo[hash_code]

    if len(nums) == 1:
        return [[], nums]
    if len(nums) == 2:
        if nums[0] == nums[1]:
            return [[], [nums[0]], nums]
        else:
            return [[], [nums[0]], [nums[1]], nums]

    result = dict()
    for i in range(0, len(nums)):
        subsets = subsets_with_dup(nums[0:i] + nums[i + 1 :], memo)
        for j in subsets:
            hash_code = hash(str(sorted(j)))
            if result.get(hash_code) is None:
                result[hash_code] = j

    result = list(result.values())
    result.append(nums)
    hash_code = hash(str(sorted(nums)))
    memo[hash_code] = result
    return result


def main():
    """
    Entrypoint
    """
    test_cases = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    ]

    for test in test_cases:
        print(sorted(subsets_with_dup(test, dict())))


if __name__ == "__main__":
    main()
