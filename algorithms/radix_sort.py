""" Radix Sort (with Counting Sort as subroutine """


def num_digits(number: int) -> int:
    """
    Returns the number of digits in a number
    """
    num = number
    count = 0

    while num > 0:
        num = num // 10
        count += 1

    return count


def new_digit_function(digit: int, length: int):
    """
    Returns a function that retrieves a digit from a number at the specified index.
    If a number's digits are fewer than the length, zeroes are prefixed on the number.
    """

    def get_digit(number: int):
        """
        Returns the specified digit from an integer
        """
        num_list = [int(x) for x in list(str(number))]
        to_add = length - len(num_list)

        for _ in range(0, to_add):
            num_list.insert(0, 0)

        num_list.reverse()

        return num_list[digit]

    return get_digit


def counting_sort(array: list, output: list, k: int, key=lambda x: x):
    """
    Counting sort algorithim by digit place
    """
    storage = [0] * (k + 1)

    for i in range(0, len(array)):
        value = key(array[i])
        storage[value] += 1

    for j in range(1, len(storage)):
        storage[j] += storage[j - 1]

    for k in range(len(array) - 1, -1, -1):
        value = key(array[k])
        output[storage[value] - 1] = array[k]
        storage[value] -= 1


def radix_sort(array: list, output: list, d: int):
    """
    Performs radix sort on input array
    """
    for i in range(0, d):
        digit_func = new_digit_function(i, d)
        # k = 9 in counting sort because a digit's max value is 9
        counting_sort(array, output, 9, digit_func)
        array = output.copy()


def main():
    """
    Entrypoint
    """
    array = [3, 53, 12, 9, 5, 89, 150, 36, 633, 233]
    output = [0] * len(array)
    d = num_digits(max(array))
    radix_sort(array, output, d)
    print(array)
    print(output)


if __name__ == "__main__":
    main()
