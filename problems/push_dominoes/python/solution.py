""" Push Dominoes """


def advance_one(dominoes: list) -> list:
    """
    Advances one turn in the state of the game
    """
    placeholder = []
    for i in range(0, len(dominoes)):
        if dominoes[i] != ".":
            placeholder.append(dominoes[i])
            continue

        if i == 0:
            if dominoes[i + 1] == "L":
                placeholder.append("L")
            else:
                placeholder.append(".")

        elif i == len(dominoes) - 1:
            if dominoes[i - 1] == "R":
                placeholder.append("R")
            else:
                placeholder.append(".")

        else:
            if dominoes[i - 1] == "R" and dominoes[i + 1] == "L":
                placeholder.append(".")
            elif dominoes[i - 1] == "L" and dominoes[i + 1] == "R":
                placeholder.append(".")
            elif dominoes[i - 1] == "R":
                placeholder.append("R")
            elif dominoes[i + 1] == "L":
                placeholder.append("L")
            else:
                placeholder.append(".")

    return placeholder


def push_dominoes(dominoes: str) -> str:
    """
    Returns the final state of the pushed dominoes
    """
    if len(dominoes) == 1:
        return dominoes
    dominoes_list = list(dominoes)
    current = "".join(dominoes_list)
    dominoes_list = advance_one(dominoes_list)
    new = "".join(dominoes_list)
    while current != new:
        current = new
        dominoes_list = advance_one(dominoes_list)
        new = "".join(dominoes_list)

    return new


def main():
    """
    Entrypoint
    """
    test_cases = [
        "RR.L",
        ".L.R...LR..L..",
    ]

    for test in test_cases:
        print(push_dominoes(test))


if __name__ == "__main__":
    main()
