""" Quicksort """


def swap_elements(array: list, index_one: int, index_two: int):
    """
    swaps two elements in a list in-place
    """
    temp = array[index_one]
    array[index_one] = array[index_two]
    array[index_two] = temp


def partition(array: list, start: int, end: int) -> int:
    """
    Partitions an array two subarrays between the pivot q, and returns the index of q

    note: we use the last element as the pivot
    """
    pivot_value = array[end]
    item_from_left = 0
    item_from_right = 0

    while True:
        for i in range(start, end + 1):  # zero-based indexing
            if array[i] >= pivot_value:
                item_from_left = i
                break

        for i in range(end - 1, start - 1, -1):
            if array[i] < pivot_value:
                item_from_right = i
                break

        if item_from_left >= item_from_right:
            break

        swap_elements(array, item_from_left, item_from_right)

    swap_elements(array, item_from_left, end)

    return item_from_left


def quicksort(array: list, start: int, end: int) -> list:
    """
    quicksort algorithm
    """
    if start < end:
        pivot_index = partition(array, start, end)
        quicksort(array, start, pivot_index - 1)
        quicksort(array, pivot_index + 1, end)


def main():
    """
    Entrypoint
    """

    array = [5, 2, 3, 7, 9, 1, 0, 6, 12, 9, 10]
    print(array)
    quicksort(array, 0, len(array) - 1)
    print(array)


if __name__ == "__main__":
    main()
