""" Top K Frequent Words """


class MaxHeap:
    """
    Implements a maximum heap data structure
    """

    def __init__(
        self, items: list, key=lambda x: x, tiebreaker=lambda child, parent: False
    ) -> None:
        self.heap = items
        self.key = key
        self.tiebreaker = tiebreaker
        self.build_max_heap()

    def __get_left_child_index(self, index: int) -> int:
        return (2 * index) + 1

    def __get_right_child_index(self, index: int) -> int:
        return (2 * index) + 2

    def __get_parent_index(self, index: int) -> int:
        return (index - 1) // 2

    def __has_left_child(self, index: int) -> bool:
        return self.__get_left_child_index(index) <= len(self.heap) - 1

    def __has_right_child(self, index: int) -> bool:
        return self.__get_right_child_index(index) <= len(self.heap) - 1

    def __has_parent(self, index: int) -> bool:
        return self.__get_parent_index(index) >= 0

    def __swap(self, index_a: int, index_b: int):
        temp = self.heap[index_a]
        self.heap[index_a] = self.heap[index_b]
        self.heap[index_b] = temp

    def max_heapify(self, index: int):
        """
        Performs the max heapify operation at the given index
        """
        left_child_index = self.__get_left_child_index(index)
        right_child_index = self.__get_right_child_index(index)
        largest = index

        if self.__has_left_child(index):
            if self.key(self.heap[left_child_index]) > self.key(self.heap[index]):
                largest = left_child_index
            elif self.key(self.heap[left_child_index]) == self.key(self.heap[index]):
                if self.tiebreaker(self.heap[left_child_index], self.heap[index]):
                    largest = left_child_index

        if self.__has_right_child(index):
            if self.key(self.heap[right_child_index]) > self.key(self.heap[largest]):
                largest = right_child_index
            elif self.key(self.heap[right_child_index]) == self.key(self.heap[largest]):
                if self.tiebreaker(self.heap[right_child_index], self.heap[largest]):
                    largest = right_child_index

        if largest != index:
            self.__swap(largest, index)
            self.max_heapify(largest)

    def build_max_heap(self):
        """
        Builds the entire max heap recursively
        """
        last_node = len(self.heap) // 2
        for i in range(last_node - 1, -1, -1):
            self.max_heapify(i)

    def peek(self):
        """
        Returns the maximum element in the heap without popping it
        """
        return self.heap[0]

    def pop(self):
        """
        Pops the maximum item in the heap
        """
        maximum = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.max_heapify(0)
        return maximum

    def insert(self, value):
        """
        Inserts a new value into the heap
        """
        self.heap.append(value)
        index = len(self.heap) - 1

        while self.__has_parent(index):
            parent = self.__get_parent_index(index)
            if self.key(self.heap[index]) > self.key(self.heap[parent]):
                self.__swap(index, parent)
                index = parent
            elif self.key(self.heap[index]) == self.key(self.heap[parent]):
                if self.tiebreaker(self.heap[index], self.heap[parent]):
                    self.__swap(index, parent)
                    index = parent
            else:
                break


def top_k_frequent(words: list, k: int) -> list:
    """
    Returns the k most frequent words in a list
    """
    hash_table = dict()

    for i in words:
        if hash_table.get(i) is None:
            hash_table[i] = 1
        else:
            hash_table[i] += 1

    hash_table = list(hash_table.items())
    heap = MaxHeap(hash_table, lambda x: x[1], lambda x, y: x[0] < y[0])

    result = []

    for _ in range(0, k):
        result.append(heap.pop()[0])

    return result


def main():
    """
    Entrypoint
    """
    test_cases = [
        (["i", "love", "leetcode", "i", "love", "coding"], 2),
        (["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4),
    ]

    for words, k in test_cases:
        print(top_k_frequent(words, k))


if __name__ == "__main__":
    main()
