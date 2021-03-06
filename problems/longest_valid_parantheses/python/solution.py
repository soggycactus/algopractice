""" Longest Valid Parantheses """


def is_valid_parantheses(string: str) -> bool:
    """
    Returns whether a string is a valid parantheses
    """

    stack = list(zip(list(string), range(len(string))))
    found = string.find("()")
    while found != -1:
        del stack[found]
        del stack[found]
        string = "".join([x[0] for x in stack])
        found = string.find("()")

    return [x[1] for x in stack]


def longest_valid_parantheses(string: str):
    """
    Returns the longest substring that has valid parantheses
    """
    result = is_valid_parantheses(string)
    if result == []:
        return string

    if len(result) == 1:
        if result[0] == 0:
            return string[1:]
        else:
            right_side = (len(string) - 1) - result[0]
            left_side = result[0]
            if right_side > left_side:
                return string[result[0] + 1 :]
            return string[0 : result[0]]

    i = 0
    j = 1
    max_length = 0
    max_pair = [0, 0]
    while j <= len(result) - 1:
        if result[j] - result[i] > max_length:
            max_length = result[j] - result[i]
            max_pair = [result[i], result[j]]
        i += 1
        j += 1

    if result[0] != 0 and result[0] > max_length:
        max_pair = [-1, result[0]]
        max_length = result[0] + 1

    if result[-1] != len(string) - 1 and len(string) - result[-1] > max_length:
        max_pair = [result[-1], len(string)]

    return string[max_pair[0] + 1 : max_pair[1]]


def main():
    """
    Entrypoint
    """
    test_cases = [
        ("(()", 2),
        (")()())", 4),
        ("", 0),
        (")())()()()((())))((((())))", 12),
        ("((()))())", 8),
        ("())(((())))()()()()", 16),
        (
            "(()(()(((())(((((()()))((((()()(()()())())())()))()()()())(())()()(((()))))()((()))(((())()((()()())((())))(())))())((()())()()((()((())))))((()(((((()((()))(()()(())))((()))()))()",
            132,
        ),
        (
            "((())())(()))(()()(()(()))(()((((()))))))((()())()))()()(()(((((()()()())))()())(()()))((((((())))((()))()()))))(()))())))()))()())((()()))))(()(((((())))))()((()(()(())((((())(())((()()(()())))())(()(())()()))())(()()()))()(((()())(((()()())))(((()()()))(()()))()))()))))))())()()((()(())(()))()((()()()((())))()(((()())(()))())())))(((()))))())))()(())))()())))())()((()))((()))()))(((())((()()()(()((()((())))((()()))())(()()(()))))())((())))(()))()))))))()(()))())(()())))))(()))((())(()((())(((((()()()(()()())))(()())()((()(()()))(()(())((()((()))))))))(()(())()())()(()(()(()))()()()(()()())))(())(()((((()()))())))(())((()(())())))))())()()))(((())))())((()(()))(()()))((())(())))))(()(()((()((()()))))))(()()()(()()()(()(())()))()))(((()(())()())(()))())))(((()))())(()((()))(()((()()()(())()(()())()(())(()(()((((())()))(((()()(((()())(()()()(())()())())(()(()()((()))))()(()))))(((())))()()))(()))((()))))()()))))((((()(())()()()((()))((()))())())(()((()()())))))))()))(((()))))))(()())))(((()))((()))())))(((()(((())))())(()))))(((()(((((((((((((())(((()))((((())())()))())((((())(((())))())(((()))))()())()(())())(()))))()))()()()))(((((())()()((()))())(()))()()(()()))(())(()()))()))))(((())))))((()()(()()()()((())((((())())))))((((((()((()((())())(()((()))(()())())())(()(())(())(()((())((())))(())())))(()()())((((()))))((()(())(()(()())))))))))((()())()()))((()(((()((()))(((((()()()()()(()(()((()(()))(()(()((()()))))()(()()((((((()((()())()))((())()()(((((()(()))))()()((()())((()())()(())((()))()()(()))",
            168,
        ),
        ("(()))())(", 4),
    ]
    for test, result in test_cases:
        parantheses = longest_valid_parantheses(test)
        print(parantheses)
        print(len(parantheses))
        assert len(parantheses) == result


if __name__ == "__main__":
    main()
