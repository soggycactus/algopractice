""" Three Sum """
from typing import List


def binarySearch(x: List[int], target: int) -> int:
    left = 0
    right = len(x) - 1

    while left <= right:
        mid = (left + right) // 2

        if x[mid] == target:
            return mid
        elif x[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None


def isTriplet(x: int, y: int, z: int) -> bool:
    if x != y and x != z and y != z:
        return (x + y + z) == 0
    return False


def threeSum(nums: List[int]) -> List[List[int]]:
    hashTable = dict()

    for i in range(0, len(nums)):
        lookup = hashTable.get(nums[i])
        if lookup is None:
            hashTable[nums[i]] = [i]
        else:
            lookup.append(i)
            hashTable[nums[i]] = lookup

    results = dict()
    for i in range(0, len(nums) - 1):
        j = i + 1
        while j < len(nums) and i != j:
            key = (nums[i] + nums[j]) * -1
            lookup = hashTable.get(key)
            if lookup is None:
                j += 1
                continue

            check = binarySearch(lookup, i)
            if check is not None:
                lookup.pop(check)
            check = binarySearch(lookup, j)
            if check is not None:
                lookup.pop(check)

            if len(lookup) > 0:
                triples = sorted([nums[i], nums[j], key])
                results[hash(str(triples))] = triples
            j += 1

    return list(results.values())


def main():
    nums = [-1, 0, 1, 2, -1, -4]

    print(threeSum(nums))


if __name__ == "__main__":
    main()
