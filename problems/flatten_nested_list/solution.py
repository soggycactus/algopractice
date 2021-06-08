""" Flatten Nested List """


def flatten(nums: list) -> list:
    """
    Flattens a deeply nested list
    """
    result = []

    for i in nums:
        if isinstance(i, int):
            result.append(i)
        else:
            result.extend(flatten(i))

    return result


def main():
    """
    Entrypoint
    """
    nums = [1, 2, 3, [1, 2, 3, [1, [[[3, 4, [5]]]]]]]
    print(flatten(nums))
    nums = [[[[4, 5, [6, 7, [[[8, 9]]]]]]]]
    print(flatten(nums))
    nums = [1, 1, 1, 1, 1]
    print(flatten(nums))


if __name__ == "__main__":
    main()
