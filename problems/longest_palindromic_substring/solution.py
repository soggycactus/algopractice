""" Longest Palindromic Substring """


def is_palindrome(s: str) -> bool:
    """
    Returns whether a string is a palindrome
    """
    palindrome = list(s)
    palindrome.reverse()
    palindrome = "".join(palindrome)
    return palindrome == s


def find_from_back(s: str, target: str) -> int:
    """
    Returns the furthermost occurence of the target in a string
    """
    for i in range(len(s) - 1, -1, -1):
        if s[i] == target:
            return i

    return -1


def longest_palindromic_substring(s: str) -> str:
    """
    Returns the longest palindrome substring of s
    """
    length = len(s)
    if length == 1:
        return s

    if length == 2:
        if s[0] == s[1]:
            return s
        else:
            return s[0]

    longest_palindrome = ""

    for i in range(0, length):
        if (length - i) < len(longest_palindrome):
            break

        end_range = length
        while (end_range - i) >= len(longest_palindrome):
            end_range = find_from_back(s[i : end_range + 1], s[i]) + i
            if end_range == i:
                break

            if end_range == -1:
                break

            palindrome = is_palindrome(s[i : end_range + 1])
            if palindrome is True and (end_range + 1) - i > len(longest_palindrome):
                longest_palindrome = s[i : end_range + 1]
                break
            else:
                end_range -= 1

    return longest_palindrome if longest_palindrome != "" else s[0]


def main():
    """
    Entrypoint
    """
    test_cases = [
        "babad",
        "cbbd",
        "a",
        "ac",
        "racecar",
        "akfasdfdsaewfqewf",
        "abcda",
        "tfekavrnnptlawqponffseumswvdtjhrndkkjppgiajjhklqpskuubeyofqwubiiduoylurzlorvnfcibxcjjzvlzfvsvwknjkzwthxxrowidmyudbtquktmyunoltklkdvzplxnpkoiikfijgulbxfxhaxnldvwmzpgaiumnvpdirlrutsqenwtihptnhghobrmmzcsrhqgdgzrvvitzgsolsxjxfeencvpnltxeetmtzlwnhlvgtbhkicivylfjhhfqteyxewmnewhmsnfdyneqoywgsgptwdlzbraksgajciebdchindegdfmayvfkwwkkfyxqjcv",
    ]
    for test in test_cases:
        print(longest_palindromic_substring(test))


if __name__ == "__main__":
    main()
