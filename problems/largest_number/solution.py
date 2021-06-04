""" Largest Number """


def swap_elements(array: list, index_a: int, index_b: int):
    """
    Swamps elements in an array
    """
    temp = array[index_a]
    array[index_a] = array[index_b]
    array[index_b] = temp


def concatenate_numbers(int_a: int, int_b: int) -> int:
    """
    Returns the concatenation of two integers
    """
    return int(str(int_a) + str(int_b))


def sort_to_largest_number(nums: list):
    """
    Sorts an array in the order that would produce the largest number when all elements are concatenated
    """
    for i in range(1, len(nums)):
        while i > 0 and concatenate_numbers(nums[i], nums[i - 1]) > concatenate_numbers(
            nums[i - 1], nums[i]
        ):
            swap_elements(nums, i, i - 1)
            i -= 1


def largest_number(nums: list) -> str:
    """
    Returns the largest possible number when all elements of the input list are concatenated
    """
    sort_to_largest_number(nums)

    while nums[0] == 0:
        if len(nums) == 1:
            break
        else:
            del nums[0]

    return "".join([str(x) for x in nums])


def main():
    """
    Entrypoint
    """
    nums = [3, 30, 34, 5, 9]
    print(largest_number(nums))
    nums = [34323, 3432]
    print(largest_number(nums))
    nums = [0, 0, 0]
    print(largest_number(nums))


if __name__ == "__main__":
    main()
