def search(nums: list, target: int) -> int:
    """
    Searches for the target in a rotated array
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + ((right - left) // 2)

        if target == nums[mid]:
            return mid

        elif nums[mid] >= nums[left]:
            if target >= nums[left] and target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:
            if target <= nums[right] and target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


def main():
    """
    Entrypoint
    """

    nums = [
        216,
        221,
        222,
        225,
        228,
        231,
        234,
        244,
        245,
        246,
        249,
        251,
        259,
        262,
        264,
        265,
        268,
        271,
        276,
        277,
        278,
        281,
        282,
        286,
        289,
        294,
        295,
        296,
        298,
        299,
        0,
        4,
        9,
        10,
        13,
        18,
        23,
        25,
        26,
        33,
        34,
        38,
        39,
        42,
        43,
        45,
        48,
        49,
        51,
        52,
        53,
        55,
        58,
        60,
        61,
        62,
        63,
        65,
        66,
        70,
        72,
        74,
        78,
        79,
        82,
        85,
        89,
        90,
        91,
        95,
        104,
        109,
        112,
        113,
        117,
        118,
        120,
        122,
        123,
        126,
        127,
        128,
        133,
        134,
        138,
        140,
        142,
        144,
        147,
        148,
        149,
        152,
        156,
        164,
        165,
        168,
        169,
        174,
        177,
        185,
        191,
        192,
        193,
        194,
        195,
        197,
        204,
        211,
        215,
    ]
    target = 0

    print(search(nums, target))


if __name__ == "__main__":
    main()
