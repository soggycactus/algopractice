""" Longest Common Prefix """
from itertools import combinations


def longest_common_prefix(str1: str, str2: str) -> str:
    """
    Returns the longest common prefix between two strings
    """
    str1 = list(str1)
    str2 = list(str2)

    common_prefix = []
    min_length = min(len(str1), len(str2))

    for i in range(0, min_length):
        if str1[i] == str2[i]:
            common_prefix.append(str1[i])
        else:
            break

    if common_prefix == []:
        return ""

    return "".join(common_prefix)


def longest_common_prefix_array(strs: list) -> list:
    """
    Returns the longest common prefix amongst all values in an array
    """
    if len(strs) == 1:
        return strs

    combos = list(combinations(strs, 2))
    results = []

    for i in combos:
        prefix = longest_common_prefix(i[0], i[1])
        results.append(prefix)

    if len(set(results)) != 1:
        results = longest_common_prefix_array(list(set(results)))

    return results


def main():
    """
    Entrypoint
    """
    strs = ["flower", "flow", "flight"]
    # strs = ["dog", "racecar", "car"]
    print(longest_common_prefix_array(strs)[0])


if __name__ == "__main__":
    main()
