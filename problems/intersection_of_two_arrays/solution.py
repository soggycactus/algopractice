""" Intersection of Two Arrays """


def binary_search(array: list, target: int) -> int:
    """
    Implements binary search
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = left + ((right - left) // 2)

        if target == array[mid]:
            return mid
        elif target < array[mid]:
            right = mid - 1
        else:
            left = mid + 1


def intersect(nums1: list, nums2: list) -> list:
    """
    Returns the intersection of two arrays
    """
    if nums1 == nums2:
        return nums1

    result = []

    if len(nums1) > len(nums2):
        nums1.sort()
        to_pop = nums1
        to_iter = nums2
    else:
        nums2.sort()
        to_pop = nums2
        to_iter = nums1

    for i in to_iter:
        index = binary_search(to_pop, i)

        if index is not None:
            result.append(to_pop.pop(index))

    return result


def main():
    """
    Entrypoint
    """

    nums1 = [1, 2, 3, 4, 5, 6, 7]
    nums2 = [7, 6, 5, 5, 3, 1, 3, 4, 4]
    print(intersect(nums1, nums2))


if __name__ == "__main__":
    main()
