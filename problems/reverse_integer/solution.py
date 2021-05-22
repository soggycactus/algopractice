""" Reverse Integer """


def reverse(number: int) -> int:
    """
    returns the reverse of x
    """
    is_negative = number < 0

    text = str(abs(number))

    output = ""
    for i in range(len(text) - 1, -1, -1):
        output += text[i]

    output = int(output)

    if output > 2 ** 31 - 1:
        return 0

    if is_negative:
        return -output

    return output


def main():
    """
    Entrypoint
    """

    number = 1534236469
    print(reverse(number))


if __name__ == "__main__":
    main()
