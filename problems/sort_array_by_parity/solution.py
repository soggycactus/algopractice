""" Sort Array By Parity """


def sort_by_parity(array: list) -> list:
    """Sorts an array by parity"""
    new_array = []
    is_even_index = True

    while array != []:
        for i in array:
            is_even_value = i % 2 == 0

            if is_even_index and is_even_value:
                new_array.append(i)
                is_even_index = False
                array.remove(i)
                continue

            if not is_even_index and not is_even_value:
                new_array.append(i)
                is_even_index = True
                array.remove(i)
                continue

            else:
                continue

    return new_array


def main():
    """Entrypoint of the program"""
    nums = [5, 2, 4, 5, 7, 4]
    print(nums)
    print(sort_by_parity(nums))


if __name__ == "__main__":
    main()
