""" First Non-Repeating Character """


def first_non_repeating_character(s):
    """
    Returns the first non-repeating character of s
    """
    hash_table = dict()

    for i in s:
        if hash_table.get(i) is None:
            hash_table[i] = 1
        else:
            hash_table[i] += 1

    for i in s:
        if hash_table[i] == 1:
            return i

    return "_"


def main():
    """
    Entrypoint
    """
    s = "abacabad"
    print(first_non_repeating_character(s))


if __name__ == "__main__":
    main()
