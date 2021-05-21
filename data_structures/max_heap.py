""" MaxHeap Data Structure """


class MaxHeap:
    """
    MaxHeap implements the heap data structure
    """

    def __init__(self, items: list = []):
        super().__init__()
        self.heap = items.copy()
        self.build_max_heap()

    def __get_left_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 1

    def __get_right_child_index(self, parent_index: int) -> int:
        return 2 * parent_index + 2

    def __get_parent_index(self, child_index: int) -> int:
        return (child_index - 1) // 2

    def __has_left_child(self, index: int) -> int:
        return self.__get_left_child_index(index) < len(self.heap)

    def __has_right_child(self, index: int) -> int:
        return self.__get_right_child_index(index) < len(self.heap)

    def __has_parent(self, index: int) -> int:
        return self.__get_parent_index(index) >= 0

    def __swap(self, index_one: int, index_two: int):
        temp = self.heap[index_one]
        self.heap[index_one] = self.heap[index_two]
        self.heap[index_two] = temp

    def peek(self) -> int:
        """
        peek returns the parent node of the heap
        """
        return self.heap[0]

    def poll(self) -> int:
        """
        poll extracts the parent node of the heap
        """
        parent = self.heap[0]
        self.__swap(0, -1)
        del self.heap[-1]
        self.max_heapify(0)
        return parent

    def max_heapify(self, index: int) -> int:
        """
        max_heapify recursively builds a max heap from an unordered array
        """
        left = self.__get_left_child_index(index)
        right = self.__get_right_child_index(index)

        if self.__has_left_child(index) and self.heap[left] > self.heap[index]:
            largest = left
        else:
            largest = index

        if self.__has_right_child(index) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.__swap(index, largest)
            self.max_heapify(largest)

    def build_max_heap(self):
        """
        build_max_heap calls max_heapify to construct a max heap

        we call max_heapify from the range (len(n) // 2) - 1
        because these indices are guaranteed to be nodes with children
        """
        last_node = len(self.heap) // 2
        # last_node minus one because of zero-based indexing
        for i in range(last_node - 1, -1, -1):
            self.max_heapify(i)

    def add(self, item: int):
        """
        add inserts a new value into the heap
        """
        self.heap.append(item)
        self.max_heapify(0)


def main():
    """
    HeapSort algorithm using MinHeap
    """
    array = [54, 1, 3, 2, 5, 4, 8, 65, 47]
    heap = MaxHeap(array)
    sorted_array = []

    for _ in range(0, len(array)):
        value = heap.poll()
        sorted_array.append(value)

    print(array)
    print(sorted_array)


if __name__ == "__main__":
    main()
