""" Buddy Strings """


def buddy_strings(a: str, b: str) -> bool:
    """
    returns true if you can swap two letters in a so the result is equal to b
    """
    if sorted(a) != sorted(b):
        return False

    if a == b:
        if len(set(sorted(a))) < len(sorted(a)):
            return True
        return False

    swaps = 0

    for i in range(0, len(a)):
        a_value = a[i]
        b_value = b[i]

        if a_value != b_value:
            swaps += 1

        if swaps > 2:
            return False

    return True


def main():
    """
    Entrypoint
    """
    string_pairs = [
        ("ab", "ba", True),
        ("ab", "ab", False),
        ("aa", "aa", True),
        ("aaaaaaabc", "aaaaaaacb", True),
        ("abdcefghi", "abcdefghi", True),
        ("abdcefghi", "abcdefgih", False),
    ]

    for i, j, k in string_pairs:
        assert buddy_strings(i, j) == k

    print("all test cases passed")


if __name__ == "__main__":
    main()
