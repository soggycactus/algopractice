""" Binary Search """


def search(nums: list, target: int) -> int:
    """
    Returns the index of the target, -1 if it doesn't exist
    """
    i = (len(nums) - 1) // 2
    forward = False
    backward = False

    while i > -1 and i < len(nums):
        if nums[i] == target:
            return i
        elif target < nums[i]:
            i -= 1
            backward = True
        else:
            i += 1
            forward = True

        if forward is True and backward is True:
            return -1

    return i if i < len(nums) else -1


def main():
    """
    Entrypoint
    """
    nums = [-1, 0, 3, 5, 9, 12]
    target = 4
    print(search(nums, target))


if __name__ == "__main__":
    main()
