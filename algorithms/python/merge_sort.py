""" Merge Sort """


def merge(array_a: list, array_b: list) -> list:
    """Merges two arrays into a single, sorted array"""
    merged_array = []

    while array_a != [] and array_b != []:
        if array_a[0] < array_b[0]:
            merged_array.append(array_a[0])
            del array_a[0]
            continue

        if array_b[0] < array_a[0]:
            merged_array.append(array_b[0])
            del array_b[0]
            continue

        if array_a[0] == array_b[0]:
            merged_array.append(array_a[0])
            del array_a[0]
            continue

    if array_a != []:
        merged_array.extend(array_a)
        array_a = []

    if array_b != []:
        merged_array.extend(array_b)
        array_b = []

    return merged_array


def merge_sort(array: list) -> list:
    """Implements the Merge Sort algorithm"""
    if len(array) == 1:
        return array

    array_a = merge_sort(array[len(array) // 2 :])
    array_b = merge_sort(array[: len(array) // 2])

    return merge(array_a, array_b)


def main():
    """Entrypoint of the program"""
    array = [1, 9, 3, 6, 2, 4, 7, 3, 21, 5, 4, 3, 7, 3, 5]
    print(array)
    print(merge_sort(array))


if __name__ == "__main__":
    main()
