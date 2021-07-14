""" Convert a Roman numeral to an integer """


def character_to_value(character: str) -> int:
    """Converts a single character to its corresponding value"""
    values = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }

    return values[character]


def roman_to_int(roman_numeral: str) -> int:
    """Converts an entire Roman Numeral to an integer value"""
    total = 0
    skip = False

    for i in range(0, len(roman_numeral)):
        if skip is True:
            skip = False
            continue
        if i == len(roman_numeral) - 1:
            total += character_to_value(roman_numeral[i])
            break

        if roman_numeral[i] == "I":
            if roman_numeral[i + 1] == "V" or roman_numeral[i + 1] == "X":
                total += character_to_value(roman_numeral[i] + roman_numeral[i + 1])
                skip = True
                continue

        if roman_numeral[i] == "X":
            if roman_numeral[i + 1] == "L" or roman_numeral[i + 1] == "C":
                total += character_to_value(roman_numeral[i] + roman_numeral[i + 1])
                skip = True
                continue

        if roman_numeral[i] == "C":
            if roman_numeral[i + 1] == "D" or roman_numeral[i + 1] == "M":
                total += character_to_value(roman_numeral[i] + roman_numeral[i + 1])
                skip = True
                continue

        total += character_to_value(roman_numeral[i])

    return total


def main():
    """Entrypoint for the program"""
    roman_numeral = "MCD"
    print(roman_numeral)
    print(roman_to_int(roman_numeral))


if __name__ == "__main__":
    main()
