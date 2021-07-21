""" Word Break """
from typing import Dict


def word_break(s: str, wordDict: Dict[str, bool], memo: Dict[str, bool]) -> bool:
    """
    Returns whether the given string can be reconstructed using the keys in a given dictionary
    """
    lookup = memo.get(s)
    if lookup is not None:
        return lookup

    if wordDict.get(s) is not None:
        memo[s] = True
        return True

    start = 0
    end = 1
    while end <= len(s):
        lookup = wordDict.get(s[start:end])
        if lookup is not None:
            if word_break(s[end:], wordDict, memo) is True:
                memo[s] = True
                return True
            else:
                end += 1
        else:
            end += 1

    memo[s] = False
    return False


def main():
    """
    Entrypoint
    """
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    wordDict = dict([(x, True) for x in wordDict])
    print(word_break(s, wordDict, dict()))


if __name__ == "__main__":
    main()
