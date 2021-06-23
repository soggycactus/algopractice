""" Group Anagrams - inplace solution """
from ast import literal_eval


def is_anagram(str1: str, str2: str) -> bool:
    """
    Returns whether a string is an anagram
    """
    if len(str1) != len(str2):
        return False
    return sorted(list(str1)) == sorted(list(str2))


def group_anagrams(strs: list) -> list:
    """
    Receives a list of strings and returns a list of grouped anagrams
    """
    result = []
    strs.sort(key=len)

    while strs != []:
        to_pop = [0]
        for i in range(1, len(strs)):
            if len(strs[0]) != len(strs[i]):
                break
            if is_anagram(strs[0], strs[i]):
                to_pop.append(i)

        result.append([strs[i] for i in to_pop])

        for i in range(len(to_pop) - 1, -1, -1):
            del strs[to_pop[i]]

    return result


def main():
    """
    Entrypoint
    """
    print("--- large test case ---")
    with open("test_input.txt", "r") as file:
        strs = literal_eval(file.read())
        print(group_anagrams(strs))

    print("--- small test case ---")
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(strs))


if __name__ == "__main__":
    main()
