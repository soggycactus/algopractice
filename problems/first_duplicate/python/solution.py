""" First Duplicate """


def first_duplicate(a):
    """
    Returns the first duplicate for which the second occurrence has the minimal index
    """
    counts = dict()
    seconds = dict()
    found = False

    for i in range(len(a)):
        count = counts.get(a[i])
        if count is None:
            counts[a[i]] = 1
        elif count == 1:
            found = True
            seconds[a[i]] = i
            counts[a[i]] += 1
        else:
            continue

    if not found:
        return -1

    return a[min(seconds.values())]


def main():
    """
    Entrypoint
    """
    a = [2, 1, 3, 5, 3, 2]
    print(first_duplicate(a))


if __name__ == "__main__":
    main()
