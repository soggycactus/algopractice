""" Counting Sort """


def counting_sort(array: list, output: list, k: int):
    """
    counting sort algorithm
    """
    storage = [0] * (k + 1)

    for i in range(0, len(array)):
        storage[array[i]] += 1

    for j in range(1, k + 1):
        storage[j] += storage[j - 1]

    for k in range(len(array) - 1, -1, -1):
        output[storage[array[k]] - 1] = array[k]
        storage[array[k]] -= 1


def main():
    """
    entrypoint
    """
    array = [5, 2, 3, 7, 9, 1, 0, 6, 12, 9, 10]
    output = [0] * len(array)
    print(array)
    counting_sort(array, output, max(array))
    print(output)


if __name__ == "__main__":
    main()
