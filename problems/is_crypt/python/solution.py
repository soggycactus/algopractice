""" Is Crypt """


def is_crypt(crypt, solution):
    """
    Returns whether the crypt & solution are valid
    """
    hash_table = dict()
    for key, value in solution:
        hash_table[key] = value

    sum = []
    for ch in crypt[2]:
        sum.append(hash_table[ch])

    if sum[0] == "0" and len(sum) != 1:
        return False

    sum = "".join(sum)
    sum = int(sum)

    first = []
    for ch in crypt[0]:
        first.append(hash_table[ch])

    if first[0] == "0" and len(first) != 1:
        return False
    first = "".join(first)
    first = int(first)

    second = []
    for ch in crypt[1]:
        second.append(hash_table[ch])

    if second[0] == "0" and len(second) != 1:
        return False
    second = "".join(second)
    second = int(second)

    return first + second == sum


def main():
    """
    Entrypoint
    """
    crypt = ["SEND", "MORE", "MONEY"]
    solution = [
        ["O", "0"],
        ["M", "1"],
        ["Y", "2"],
        ["E", "5"],
        ["N", "6"],
        ["D", "7"],
        ["R", "8"],
        ["S", "9"],
    ]
    print(is_crypt(crypt, solution))


if __name__ == "__main__":
    main()
