""" Binary Search Algorithm """


def binary_search(array: list, target: int):
    """
    Performs a binary search for the target
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        mid = left + ((right - left) // 2)

        if array[mid] == target:
            return mid
        elif target < array[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return False


def main():
    """
    Entrypoint
    """
    array = [1, 2, 3, 4, 5, 7, 12, 23]
    print(binary_search(array, 3))
    print(binary_search(array, 5))
    print(binary_search(array, 1))
    print(binary_search(array, 23))
    print(binary_search(array, 13))


if __name__ == "__main__":
    main()
