""" Group Anagrams - filter solution """
from ast import literal_eval


def group_anagrams(strs: list) -> list:
    """
    Receives a list of strings and returns a list of grouped anagrams
    """
    hash_table = dict()

    for word in strs:
        anagram = "".join(sorted(list(word)))
        if hash_table.get(anagram) is None:
            hash_table[anagram] = [word]
        else:
            hash_table[anagram].append(word)

    return list(hash_table.values())


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
