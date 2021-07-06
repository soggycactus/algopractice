""" Reshape the Matrix """


def flatten(array: list):
    """
    Flattens a nested array
    """
    result = []

    for i in array:
        if isinstance(i, int):
            result.append(i)
        else:
            result.extend(flatten(i))

    return result


def matrix_reshape(mat: list, r: int, c: int) -> list:
    """
    Reshapes a matrix into the specified r x c matrix, if possible
    """
    if r * c != len(mat) * len(mat[0]):
        return mat

    result = []
    for _ in range(r):
        result.append([0] * c)

    values = flatten(mat)

    for i in range(r):
        for j in range(c):
            result[i][j] = values.pop(0)

    return result


def main():
    """
    Entrypoint
    """
    test = [[1, 2], [3, 4]]
    r = 1
    c = 4
    print(matrix_reshape(test, r, c))


if __name__ == "__main__":
    main()
