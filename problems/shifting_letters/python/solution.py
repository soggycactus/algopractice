""" Shifting Letters """
from typing import List
from string import ascii_lowercase as alphabet


def shifting_letters(s: str, shifts: List[int]) -> str:
    """
    Shifts the letters in s according to shifts
    """
    result = []
    running_sum = 0

    for i in range(len(s) - 1, -1, -1):
        current = alphabet.index(s[i])
        shift = running_sum + shifts[i]
        iterations = current + shift

        if iterations > 25:
            index = iterations % 26
        else:
            index = iterations

        result.append(alphabet[index])
        running_sum += shifts[i]

    result.reverse()
    return "".join(result)


def main():
    """
    Entrypoint
    """
    s = "abc"
    shifts = [3, 5, 9]
    print(shifting_letters(s, shifts))


if __name__ == "__main__":
    main()
