""" Custom Sort String """


def swap(array: list, a: int, b: int):
    """
    Swaps two elements in an array inplace
    """
    temp = array[a]
    array[a] = array[b]
    array[b] = temp


def insertion_sort(array: list, key=lambda x: x):
    """
    Performs insertion sort on an array
    """
    for i in range(1, len(array)):
        while i > 0:
            before = key(array[i - 1])
            after = key(array[i])

            if before is None and after is None:
                break
            elif before is None and after is not None:
                swap(array, i, i - 1)
                i -= 1
            elif before is not None and after is None:
                i -= 1
            elif after < before:
                swap(array, i, i - 1)
                i -= 1
            else:
                break


def custom_sort_string(order: str, str: str) -> str:
    """
    Performs a custom sort on the string according to the order
    """
    hash_table = dict()
    for i in range(0, len(order)):
        hash_table[order[i]] = i

    str = list(str)
    insertion_sort(str, lambda x: hash_table.get(x))

    return "".join(str)


def main():
    """
    Entrypoint
    """
    test_cases = [
        ("cba", "abcd"),
        ("zxyghi", "gasdwzchsycxzyaisdghahsdgiyxhii"),
    ]
    for order, string in test_cases:
        print("Order:  ", order)
        print("Before: ", string)
        new_string = custom_sort_string(order, string)
        print("After:  ", new_string)
        print()


if __name__ == "__main__":
    main()
