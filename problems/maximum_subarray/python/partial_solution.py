""" Maximum Subarray """


def max_subarray(nums: list, memo: dict) -> int:
    """
    Returns the sum of the max subarray
    """
    lookup = memo.get(str(nums))
    if lookup is not None:
        return lookup

    length = len(nums)
    if length == 1:
        return nums[0]

    if len(list(filter(lambda x: x >= 0, nums))) == length:
        return sum(nums)

    left_side = memo.get(str(nums[0 : length - 1]))
    if left_side is None:
        left_side = max_subarray(nums[0 : length - 1], memo)
        memo[str(nums[0 : length - 1])] = left_side

    right_side = memo.get(str([nums[1:length]]))
    if right_side is None:
        right_side = max_subarray(nums[1:length], memo)
        memo[str(nums[0:length])] = right_side

    return max(left_side, right_side, sum(nums))


def main():
    """
    Entrypoint
    """
    test_cases = [
        [5, 4, 1, -2, -3],
        [5, 4, -1, 7, 8],
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],
        [1],
        [
            1,
            2,
            -3,
            4,
            -6,
            4,
            2,
            2,
            -3,
            4,
            -5,
            6,
            3,
            2,
            1,
            -2,
            34,
            -5,
            -4,
            2,
            3,
            1,
            -23,
            5,
            4,
            5,
            23,
            -4,
            1,
            234,
            -34,
            4,
            5,
            1,
            6,
            45,
            34,
            523,
            -42,
            -34,
            -124,
            -12,
            -4,
            -234123,
            12,
            34,
            123,
            2,
            -23,
            1,
            43,
            -2,
            -34,
            -234,
        ],
        [0, -2, -3],
    ]
    for test in test_cases:
        print(max_subarray(test, dict()))


if __name__ == "__main__":
    main()
