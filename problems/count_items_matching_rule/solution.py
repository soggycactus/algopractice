""" Count Items Matching Rule """


def count_matches(items: list, ruleKey: str, ruleValue: str) -> int:
    """
    Returns the number of matches in items
    """
    if ruleKey == "type":
        return len(list(filter(lambda x: x[0] == ruleValue, items)))
    elif ruleKey == "color":
        return len(list(filter(lambda x: x[1] == ruleValue, items)))
    else:
        return len(list(filter(lambda x: x[2] == ruleValue, items)))


def main():
    """
    Entrypoint
    """
    items = [
        ["phone", "blue", "pixel"],
        ["computer", "silver", "lenovo"],
        ["phone", "gold", "iphone"],
    ]
    print(count_matches(items, "color", "silver"))
    print(count_matches(items, "type", "phone"))


if __name__ == "__main__":
    main()
