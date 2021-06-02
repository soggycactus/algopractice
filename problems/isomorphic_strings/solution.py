""" Isomorphic Strings """


def is_isomorphic(s: str, t: str) -> bool:
    """
    Returns whether two strings are isomorphic
    """
    character_map = dict()

    for i in range(0, len(s)):
        character_map[s[i]] = t[i]

    if len(set(character_map.keys())) != len(set(character_map.values())):
        return False

    r = []
    for i in s:
        r.append(character_map[i])

    return "".join(r) == t


def main():
    """
    Entrypoint
    """
    test_cases = [
        ("title", "paper"),
        ("paper", "title"),
        ("egg", "add"),
        ("foo", "bar"),
        ("racebar", "racecar"),
        ("raccear", "racecar"),
        ("racecar", "racecar"),
    ]

    for i, j in test_cases:
        print(is_isomorphic(i, j))


if __name__ == "__main__":
    main()
