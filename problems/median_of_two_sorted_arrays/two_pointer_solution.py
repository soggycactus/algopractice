""" Median of Two Sorted Arrays """


class Stack:
    def __init__(self, length) -> None:
        self.items = []
        self.length = length

    def push(self, value):
        if len(self.items) < self.length:
            self.items.append(value)
        else:
            del self.items[0]
            self.items.append(value)

    def pop(self):
        return self.items.pop()


def median_two_sorted_arrays(nums1: list, nums2: list) -> float:
    n1 = len(nums1)
    n2 = len(nums2)
    total = n1 + n2
    median = (total) // 2

    i = 0
    j = 0
    stack = Stack(length=2)

    for _ in range(0, median + 1):
        if i == n1:
            stack.push(nums2[j])
            j += 1
        elif j == n2:
            stack.push(nums1[i])
            i += 1
        elif nums1[i] < nums2[j]:
            stack.push(nums1[i])
            i += 1
        else:
            stack.push(nums2[j])
            j += 1

    if total % 2 == 0:
        last = stack.pop()
        first = stack.pop()
        return (first + last) / 2

    return stack.pop()


def main():
    test_cases = [
        [[1, 2], [3, 4]],
        [[1, 3], [2]],
        [[0, 0], [0, 0]],
        [[], [1]],
        [[2], []],
        [[1, 2, 5, 6, 7, 9, 12, 15, 67], [4, 6, 7, 9, 10, 11, 22, 45, 78]],
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]],
        [[2], [1, 3, 4, 5, 6]],
        [[2], [1, 3, 4, 5, 6, 7, 8]],
    ]

    for i, j in test_cases:
        print(median_two_sorted_arrays(i, j))


if __name__ == "__main__":
    main()
