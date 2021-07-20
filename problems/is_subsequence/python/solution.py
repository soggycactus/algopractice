""" Is Subsequence """


def is_subsequence(s: str, t: str) -> bool:
    """
    Returns whether s is a subsequence of t
    """
    indices = []
    previous = -1
    hash_table = dict()

    for i in range(0, len(t)):
        if hash_table.get(t[i]) is not None:
            hash_table[t[i]].append(i)
        else:
            hash_table[t[i]] = [i]

    for l in s:
        lookup = hash_table.get(l)
        if lookup is None or lookup == []:
            return False
        found = False
        for i in range(0, len(lookup)):
            if lookup[i] > previous:
                previous = lookup.pop(i)
                indices.append(previous)
                found = True
                break

        if found is False:
            return False

    return sorted(indices) == indices


def main():
    """
    Entrypoint
    """
    test_cases = [
        ("zfdasdfywasldf", "zffdasdfywasldf"),
    ]

    for s, t in test_cases:
        print(is_subsequence(s, t))


if __name__ == "__main__":
    main()
