""" Smallest Letter Greater Than Target """


def next_greatest_letter(letters: list, target: str) -> str:
    """
    Returns the next greatest letter in letters according to target, while also wrapping the list.
    """
    left = 0
    right = len(letters) - 1

    while left <= right:
        mid = left + ((right - left) // 2)

        if target == letters[mid]:
            if mid == len(letters) - 1:
                return letters[0]

            mid_plus = mid
            while mid_plus <= len(letters) - 1:
                if letters[mid_plus] == letters[mid]:
                    mid_plus += 1
                else:
                    break

            if mid_plus > len(letters) - 1:
                return letters[0]

            return letters[mid_plus]

        elif target < letters[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return letters[left] if left <= len(letters) - 1 else letters[0]


def main():
    """
    Entrypoint
    """
    letters = ["c", "f", "j"]
    print(next_greatest_letter(letters, "a"))
    print(next_greatest_letter(letters, "c"))
    print(next_greatest_letter(letters, "d"))
    print(next_greatest_letter(letters, "g"))
    print(next_greatest_letter(letters, "j"))
    letters = ["e", "e", "e", "e", "e", "e", "n", "n", "n", "n"]
    print(next_greatest_letter(letters, "e"))

    letters = ["c", "e", "e", "e", "e", "e"]
    print(next_greatest_letter(letters, "e"))


if __name__ == "__main__":
    main()
