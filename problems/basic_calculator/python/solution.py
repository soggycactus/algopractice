""" Basic Calculator """


def find_close(s, i):
    """
    Finds the index of the closing bracket of a string, given the index of the starting bracket
    """
    count = 0
    for j in range(i + 1, len(s)):
        if s[j] == ")":
            if count == 0:
                return j
            else:
                count -= 1
        elif s[j] == "(":
            count += 1
        else:
            continue


def calculate(s: str) -> int:
    """
    Calculates the result of a mathematical string
    """
    current = ""
    result = 0
    is_positive = True
    i = 0

    while i < len(s):
        ch = s[i]

        if ch.isdigit():
            current = current + ch

        elif ch == "+":
            if current == "":
                pass
            elif is_positive:
                result += int(current)
            else:
                result -= int(current)
                is_positive = True
            current = ""

        elif ch == "-":
            if current == "":
                pass
            elif is_positive:
                result += int(current)
            else:
                result -= int(current)
            current = ""
            is_positive = False

        elif ch == "(":
            end = find_close(s, i)
            inner = calculate(s[i + 1 : end])
            if is_positive:
                result += inner
            else:
                result -= inner
                is_positive = True
            i = end

        i += 1

    if current == "":
        return result

    if is_positive:
        result += int(current)
    else:
        result -= int(current)

    return result


def main():
    """
    Entrypoint
    """
    test_cases = [
        "1 + 1",
        " 2-1 + 2 ",
        "(1+(4+5+2)-3)+(6+8)",
        "1+(4+5+2)-3",
        "(7)-(0)+(4)",
    ]

    for test in test_cases:
        print(calculate(test))


if __name__ == "__main__":
    main()
