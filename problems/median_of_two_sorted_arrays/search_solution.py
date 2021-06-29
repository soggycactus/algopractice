""" Median of Two Sorted Arrays """


def binary_search(array: list, target: int):
    """
    Performs binary search. Returns the index where the target would be found if not found.
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

    return mid if target < array[mid] else mid + 1


def insert_in_place(array: list, value: int):
    """
    Inserts an element into a sorted list in place
    """
    position = binary_search(array, value)
    temp = array[position:]
    del array[position:]

    array.append(value)

    for _ in range(0, len(temp)):
        array.append(temp.pop(0))


def median_two_sorted_arrays(nums1: list, nums2: list) -> float:
    total_sum = len(nums1) + len(nums2)
    median = (total_sum) // 2

    if nums1 == [] and nums2 != []:
        if len(nums2) == 1:
            return nums2[0]

        if len(nums2) % 2 == 0:
            return (nums2[median] + nums2[median - 1]) / 2

        return nums2[median]

    if nums2 == [] and nums1 != []:
        if len(nums1) == 1:
            return nums1[0]

        if len(nums1) % 2 == 0:
            return (nums1[median] + nums1[median - 1]) / 2

        return nums1[median]

    if nums1[-1] < nums2[-1]:
        smaller_list = nums1
        bigger_list = nums2
    else:
        smaller_list = nums2
        bigger_list = nums1

    overlap = binary_search(bigger_list, smaller_list[-1])

    if overlap == 0:
        if median <= len(smaller_list) - 1:
            if total_sum % 2 == 0:
                return (smaller_list[median] + smaller_list[median - 1]) / 2

            return smaller_list[median]

        else:
            index = median - len(smaller_list)
            if total_sum % 2 == 0:
                if index == 0:
                    return (smaller_list[-1] + bigger_list[index]) / 2

                return (bigger_list[index] + bigger_list[index - 1]) / 2

            return bigger_list[index]

    else:
        for _ in range(0, overlap + 1):
            insert_in_place(smaller_list, bigger_list.pop(0))

        for _ in range(0, len(bigger_list)):
            smaller_list.append(bigger_list.pop(0))

        if total_sum % 2 == 0:
            return (smaller_list[median] + smaller_list[median - 1]) / 2

        return smaller_list[median]


def main():
    test_cases = [
        [[1, 2], [3, 4]],
        [[1, 3], [2]],
        [[0, 0], [0, 0]],
        [[], [1]],
        [[2], []],
        [[1, 2, 5, 6, 7, 9, 12, 15, 67], [4, 6, 7, 9, 10, 11, 22, 45, 78]],
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]],
        [[2], [1, 3, 4, 5, 6]],
        [[2], [1, 3, 4, 5, 6, 7, 8]],
    ]

    for i, j in test_cases:
        print(median_two_sorted_arrays(i, j))


if __name__ == "__main__":
    main()
