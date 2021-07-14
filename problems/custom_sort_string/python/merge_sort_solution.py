""" Custom Sort String """


def merge(array_a: list, array_b: list, key=lambda x: x) -> list:
    """Merges two arrays into a single, sorted array"""
    merged_array = []
    placeholder = []

    while array_a != [] and array_b != []:
        a = key(array_a[0])
        b = key(array_b[0])

        if a is None and b is None:
            placeholder.append(array_a[0])
            del array_a[0]
            placeholder.append(array_b[0])
            del array_b[0]

        elif a is None and b is not None:
            placeholder.append(array_a[0])
            del array_a[0]

        elif a is not None and b is None:
            placeholder.append(array_b[0])
            del array_b[0]

        elif a < b:
            merged_array.append(array_a[0])
            del array_a[0]

        elif b < a:
            merged_array.append(array_b[0])
            del array_b[0]

        else:
            merged_array.append(array_a[0])
            del array_a[0]

    if array_a != []:
        merged_array.extend(array_a)
        array_a = []

    if array_b != []:
        merged_array.extend(array_b)
        array_b = []

    merged_array.extend(placeholder)

    return merged_array


def merge_sort(array: list, key=lambda x: x) -> list:
    """Implements the Merge Sort algorithm"""
    if len(array) == 1:
        return array

    array_a = merge_sort(array[len(array) // 2 :], key)
    array_b = merge_sort(array[: len(array) // 2], key)

    return merge(array_a, array_b, key)


def custom_sort_string(order: str, str: str) -> str:
    """
    Performs a custom sort on the string according to the order
    """
    hash_table = dict()
    for i in range(0, len(order)):
        hash_table[order[i]] = i

    str = list(str)
    str = merge_sort(str, lambda x: hash_table.get(x))

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
