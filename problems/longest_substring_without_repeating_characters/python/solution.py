""" Longest Substring Without Repeating Characters """


def length_of_longest_substring(s: str) -> int:
    """
    Returns the length of the longest substring without repeating characters
    """
    max_length = 0
    hash_table = dict()
    count = 0
    i = 0
    while i < len(s):
        if hash_table.get(s[i]) is not None:
            if count > max_length:
                max_length = count
            count = 0
            i = hash_table.get(s[i]) + 1
            hash_table = dict()
        hash_table[s[i]] = i
        count += 1
        i += 1

    if count > max_length:
        max_length = count

    return max_length


def main():
    """
    Entrypoint
    """
    test_cases = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "",
        "aldhfwuofuansduhqwieyubfcusadhfoqwieuhflaiusdhfiuqwebfalsdjfhiqwuefhalsdhfailuwehfuioqehwfaliuwhefaliusdhf",
    ]
    for test in test_cases:
        print(length_of_longest_substring(test))


if __name__ == "__main__":
    main()
