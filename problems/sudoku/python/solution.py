""" Sudoku """


def sudoku2(grid):
    """
    Returns whether the grid is a valid sudoku puzzle
    """
    for row in grid:
        hash_table = dict()
        for value in row:
            if value == ".":
                continue
            else:
                if hash_table.get(value) is not None:
                    return False
                hash_table[value] = True

    for column in range(0, len(grid)):
        hash_table = dict()
        for row in range(0, len(grid)):
            value = grid[row][column]
            if value == ".":
                continue
            else:
                if hash_table.get(value) is not None:
                    return False
                hash_table[value] = True

    for rows in [[0, 3], [3, 6], [6, 9]]:
        for columns in [[0, 3], [3, 6], [6, 9]]:
            hash_table = dict()
            for row in range(rows[0], rows[1]):
                for column in range(columns[0], columns[1]):
                    value = grid[row][column]
                    if value == ".":
                        continue
                    else:
                        if hash_table.get(value) is not None:
                            return False
                        hash_table[value] = True

    return True


def main():
    """
    Entrypoint
    """
    test_cases = [
        [
            [".", ".", ".", "1", "4", ".", ".", "2", "."],
            [".", ".", "6", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", "1", ".", ".", ".", ".", ".", "."],
            [".", "6", "7", ".", ".", ".", ".", ".", "9"],
            [".", ".", ".", ".", ".", ".", "8", "1", "."],
            [".", "3", ".", ".", ".", ".", ".", ".", "6"],
            [".", ".", ".", ".", ".", "7", ".", ".", "."],
            [".", ".", ".", "5", ".", ".", ".", "7", "."],
        ],
        [
            [".", ".", ".", ".", "2", ".", ".", "9", "."],
            [".", ".", ".", ".", "6", ".", ".", ".", "."],
            ["7", "1", ".", ".", "7", "5", ".", ".", "."],
            [".", "7", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", "8", "3", ".", ".", "."],
            [".", ".", "8", ".", ".", "7", ".", "6", "."],
            [".", ".", ".", ".", ".", "2", ".", ".", "."],
            [".", "1", ".", "2", ".", ".", ".", ".", "."],
            [".", "2", ".", ".", "3", ".", ".", ".", "."],
        ],
    ]

    for test in test_cases:
        print(sudoku2(test))


if __name__ == "__main__":
    main()
