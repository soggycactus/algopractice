""" Insertion Sort """


def insertion_sort(array: list) -> list:
    """
    Implements the insertion sort algorithm
    """
    # [2,5,4,7,1,2]
    for i in range(1, len(array)):
        while i > 0 and array[i - 1] > array[i]:
            temp = array[i]
            array[i] = array[i - 1]
            array[i - 1] = temp
            i -= 1


def main():
    """
    Entrypoint to the program
    """
    array = [5, 1, 3, 2, 3, 6, 8, 2, 4, 8, 90, 2, 3]
    print(array)
    insertion_sort(array)
    print(array)


if __name__ == "__main__":
    main()
