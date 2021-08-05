""" Minimum to Remove to Make Valid Parantheses """


def min_remove_to_make_valid(s: str) -> str:
    """
    Removes the minimum number of parantheses to make the string valid
    """
    count = 0
    stack = []

    i = 0
    while i < len(s):
        ch = s[i]

        if ch == "(":
            count += 1
            stack.append(i)
            i += 1
        elif ch == ")":
            if count == 0:
                temp = list(s)
                temp.pop(i)
                s = "".join(temp)
                i -= 1
            else:
                count -= 1
                stack.pop()
            i += 1
        else:
            i += 1

    temp = list(s)
    for i in range(len(stack) - 1, -1, -1):
        temp.pop(stack[i])

    return "".join(temp)
