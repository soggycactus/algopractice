""" Valid Parantheses """


def matching_value(s: str) -> str:
    """
    Returns the matching value of 's'
    """
    values = {
        "(": ")",
        "{": "}",
        "[": "]",
        ")": False,
        "}": False,
        "]": False,
    }

    return values[s]


def is_valid(s: str) -> bool:
    """
    Returns whether the string has valid parantheses
    """
    if len(s) == 1 or len(s) % 2 != 0:
        return False

    match = matching_value(s[0])
    if not match:
        return False

    if match == s[1]:
        if len(s) == 2:
            return True

        return is_valid(s[2:])

    for i in range(len(s) - 1, 0, -1):

        if s[i] == match and i == len(s) - 1:
            if is_valid(s[1:i]):
                return True
            else:
                continue

        elif s[i] == match and i == 1:
            if is_valid(s[i + 1 :]):
                return True
            else:
                continue

        elif s[i] == match:
            if is_valid(s[1:i]) and is_valid(s[i + 1 :]):
                return True
            else:
                continue

    return False


def main():
    """
    Entrypoint
    """
    s = [
        "(([]){})",
        "{}[{}]((){})(){}",
        "((){})(){}",
        "(()[])()",
        "()[]{}",
        "()()[]{}",
        "{[]}",
        "{}[{}]((){})(){}",
    ]

    for i in s:
        print(is_valid(i))


if __name__ == "__main__":
    main()
