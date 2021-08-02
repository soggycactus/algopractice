""" Valid Parantheses """


class Stack:
    """
    Represents a simple stack
    """

    def __init__(self) -> None:
        self.items = []

    def push(self, value):
        """
        Pushes a new value onto the stack
        """
        self.items.append(value)

    def pop(self, value) -> bool:
        """
        Pops a value off of the stack
        """
        if self.items == []:
            return False

        if value == ")":
            if self.items.pop() != "(":
                return False
            else:
                return True
        elif value == "}":
            if self.items.pop() != "{":
                return False
            else:
                return True
        elif value == "]":
            if self.items.pop() != "[":
                return False
            else:
                return True


def is_valid(s: str) -> bool:
    """
    Returns whether the parantheses are valid
    """
    stack = Stack()

    for i in range(0, len(s)):
        if s[i] == "(":
            stack.push(s[i])
        elif s[i] == ")":
            if stack.pop(s[i]) is False:
                return False
        elif s[i] == "{":
            stack.push(s[i])
        elif s[i] == "}":
            if stack.pop(s[i]) is False:
                return False
        elif s[i] == "[":
            stack.push(s[i])
        elif s[i] == "]":
            if stack.pop(s[i]) is False:
                return False

    return stack.items == []


def main():
    """
    Entrypoint
    """
    s = [
        ("(([]){})", True),
        ("{}[{}]((){})(){}", True),
        ("((){})(){}", True),
        ("(()[])()", True),
        ("()[]{}", True),
        ("()()[]{}", True),
        ("{[]}", True),
        ("{}[{}]((){})(){}", True),
        ("([)]", False),
        ("({[]})", True),
    ]

    for test, result in s:
        assert is_valid(test) == result


if __name__ == "__main__":
    main()
