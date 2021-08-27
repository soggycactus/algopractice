""" Rotate image """


def rotate_image(a):
    """
    Rotates an n x n 2D matrix by 90 degrees
    """
    result = []
    for _ in range(len(a)):
        result.append([0] * len(a))

    for i in range(len(a)):
        column = len(a) - 1 - i
        row = 0
        for value in a[i]:
            result[row][column] = value
            row += 1

    return result


def main():
    """
    Entrypoint
    """
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate_image(a))


if __name__ == "__main__":
    main()
