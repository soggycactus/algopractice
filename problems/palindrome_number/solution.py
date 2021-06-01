""" Palindrome Number """


def is_palindrome(x: int) -> bool:
    """
    Returns whether x is a palindrome number
    """
    x = list(str(x))
    y = []
    for i in range(len(x) - 1, -1, -1):
        y.append(x[i])

    return x == y


def main():
    """
    Entrypoint
    """
    x = 12121
    print(is_palindrome(x))


if __name__ == "__main__":
    main()
