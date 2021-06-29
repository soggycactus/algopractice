""" Longest Palindrome """


def longest_palindrome_length(s: str) -> str:
    """
    Returns the longest palindrome that can be built with the letters in s
    """
    hash_table = dict()

    for i in list(s):
        if hash_table.get(i) is not None:
            hash_table[i] += 1
        else:
            hash_table[i] = 1

    used_odd_number = False
    total_characters = 0

    for value in sorted(hash_table.values(), reverse=True):
        if value % 2 != 0 and used_odd_number is False:
            used_odd_number = True
            total_characters += value
            continue

        if value % 2 != 0:
            value -= 1
            total_characters += value
            continue
        else:
            total_characters += value

    return total_characters


def main():
    """
    Entrypoint
    """
    test_cases = [
        "abccccdd",
        "a",
        "bb",
        "cccddd",
        "cccccdd",
    ]

    for test in test_cases:
        print(longest_palindrome_length(test))


if __name__ == "__main__":
    main()
