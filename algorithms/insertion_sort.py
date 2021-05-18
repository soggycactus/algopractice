""" Insertion Sort """


def insertion_sort(array: list) -> list:
    """
    Implements the insertion sort algorithm
    """
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            first = array[i]
            second = array[j]

            if first > second:
                array[i] = second
                array[j] = first

    return array


def main():
    """
    Entrypoint to the program
    """
    array = [5, 1, 3, 2, 3, 6, 8, 2, 4, 8, 90, 2, 3]
    print(array)
    print(insertion_sort(array))


if __name__ == "__main__":
    main()
