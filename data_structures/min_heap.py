""" MinHeap Data Structure """
from random import randint


class MinHeap:
    """MinHeap"""

    def __init__(self, items: list = []):
        super().__init__()
        self.heap = items.copy()
        self.build_min_heap()

    def __get_left_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 1

    def __get_right_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 2

    def __get_parent_index(self, child_index: int) -> int:
        return (child_index - 1) // 2

    def __has_left_child(self, index: int) -> bool:
        return self.__get_left_child_index(index) < len(self.heap)

    def __has_right_child(self, index: int) -> bool:
        return self.__get_right_child_index(index) < len(self.heap)

    def __has_parent(self, index: int) -> bool:
        return self.__get_parent_index(index) >= 0

    def __swap(self, index_one: int, index_two: int):
        temp = self.heap[index_one]
        self.heap[index_one] = self.heap[index_two]
        self.heap[index_two] = temp

    def peek(self) -> int:
        """
        Returns the parent node of the heap
        """
        return self.heap[0]

    def poll(self) -> int:
        """
        Pops the parent node of the heap & rebuilds the heap
        """
        poll = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        del self.heap[-1]
        self.min_heapify(0)
        return poll

    def min_heapify(self, index: int):
        """
        recursively builds a min heap from an unordered array
        """
        left = self.__get_left_child_index(index)
        right = self.__get_right_child_index(index)

        if self.__has_left_child(index) and self.heap[left] < self.heap[index]:
            smallest = left

        else:
            smallest = index

        if self.__has_right_child(index) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != index:
            self.__swap(index, smallest)
            self.min_heapify(smallest)

    def build_min_heap(self):
        """
        build_min_heap calls min_heapify to construct a min heap

        we call min_heapify from the range (len(n) // 2) - 1
        because these indices are guaranteed to be nodes with children
        """
        last_node = len(self.heap) // 2
        # last_node minus one because of zero-based indexing
        for i in range(last_node - 1, -1, -1):
            self.min_heapify(i)

    def add(self, item: int):
        """
        Adds a new item to the heap
        """
        self.heap.append(item)
        self.min_heapify(0)


def main():
    """
    HeapSort algorithm using MinHeap
    """
    # array = [54, 1, 3, 2, 5, 4, 8, 65, 47]
    array = [randint(0, 100000000000) for _ in range(1000000)]
    heap = MinHeap(array)
    sorted_array = []

    for _ in range(0, len(array)):
        value = heap.poll()
        sorted_array.append(value)

    # print(array)
    # print(sorted_array)


if __name__ == "__main__":
    main()
