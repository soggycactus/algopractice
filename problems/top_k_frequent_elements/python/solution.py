""" Top K Frequent Elements """


def top_k_frequent(nums: list, k: int) -> list:
    """
    Returns the top k frequent elements in a list
    """
    hash_table = dict()

    for i in nums:
        if hash_table.get(i) is None:
            hash_table[i] = 1
        else:
            hash_table[i] += 1

    hash_table = sorted(list(hash_table.items()), key=lambda x: x[1])
    hash_table.reverse()
    return [x[0] for x in hash_table[:k]]


def main():
    """
    Entrypoint
    """
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(top_k_frequent(nums, k))


if __name__ == "__main__":
    main()
