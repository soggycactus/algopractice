""" Letter Combinations of Phone Number """

hash_table = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
}


def letter_combinations(digits: str) -> list:
    """
    Returns all possible letter combinations of phone number
    """
    if digits == "":
        return []

    store = hash_table.get(int(digits[0]))

    for i in digits[1:]:
        ch = hash_table.get(int(i))
        new_store = []
        for item in store:
            new_store.extend([item + x for x in ch])
        store = new_store

    return store


def main():
    """
    Entrypoint
    """
    test_cases = [
        "23",
        "2",
        "927",
        "2794",
    ]
    for test in test_cases:
        print(letter_combinations(test))


if __name__ == "__main__":
    main()
