""" Palindrome String """


def is_palindrome(s: str) -> bool:
    """
    Returns whether a string is a palindrome
    """
    original = [x.lower() for x in list(s) if x.isalnum()]
    reverse = original.copy()
    reverse.reverse()

    return reverse == original


def main():
    """
    Entrypoint
    """
    s = "A man, a plan, a canal: Panama"
    print(is_palindrome(s))


if __name__ == "__main__":
    main()
