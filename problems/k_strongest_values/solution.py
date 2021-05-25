""" K Strongest Values """


def get_strongest(arr: list, k: int) -> list:
    """
    returns the k strongest numbers in arr
    """
    arr.sort()
    median = arr[(len(arr) - 1) // 2]

    strength = [(abs(x - median), x) for x in arr]
    strength.sort(reverse=True)

    output = [x[1] for x in strength[:k]]
    return output


def main():
    """
    entrypoint
    """
    array = [1, 1, 3, 5, 5]
    k = 2
    print(get_strongest(array, k))


if __name__ == "__main__":
    main()
