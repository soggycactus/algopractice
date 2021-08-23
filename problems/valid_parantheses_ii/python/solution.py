""" Valid Parantheses II """


class Stack:
    """
    Represents a simple Stack
    """

    def __init__(self):
        self.left = []
        self.special = []

    def push(self, value, index):
        """
        Pushes a new value to the stack
        """
        if value == "(":
            self.left.append((value, index))
        elif value == "*":
            self.special.append((value, index))

    def pop(self):
        """
        Pops a value from the stack if available
        """
        if len(self.left) == 0:
            if len(self.special) == 0:
                return
            return self.special.pop()
        return self.left.pop()


def check(s: str) -> bool:
    """
    Checks if a string has valid parantheses
    """
    stack = Stack()

    for i in range(0, len(s)):
        if s[i] == "(":
            stack.push(s[i], i)
        elif s[i] == "*":
            stack.push(s[i], i)
        else:
            pop = stack.pop()
            if pop is None:
                return False

    if len(stack.left) == 0:
        return True

    remaining = stack.left + stack.special
    remaining.sort(key=lambda x: x[1])
    counter = 0

    for i in range(0, len(remaining)):
        ch = remaining[i][0]
        if ch == "(":
            counter += 1
        else:
            if counter > 0:
                counter -= 1

    return counter == 0


def main():
    """
    Entrypoint
    """
    test_cases = [
        "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())",
        "(((((*(*********((*(((((****",
        "()",
        "(*)",
        "(*))",
        "(((*)",
        "(((****)",
    ]
    for test in test_cases:
        print(check(test))


if __name__ == "__main__":
    main()
