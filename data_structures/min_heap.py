""" MinHeap Data Structure """


class MinHeap:
    """MinHeap"""

    def __init__(self, items: list = []):
        super().__init__()
        self.heap = items.copy()
        self.heapify_up()
        self.heapify_down()

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

    def __get_left_child(self, index: int) -> int:
        return self.heap[self.__get_left_child_index(index)]

    def __get_right_child(self, index: int) -> int:
        return self.heap[self.__get_right_child_index(index)]

    def __get_parent(self, index: int) -> int:
        return self.heap[self.__get_parent_index(index)]

    def __swap(self, index_one: int, index_two: int):
        temp = self.heap[index_one]
        self.heap[index_one] = self.heap[index_two]
        self.heap[index_two] = temp

    def peek(self) -> int:
        """Returns the parent node of the heap"""
        return self.heap[0]

    def poll(self) -> int:
        """Pops the parent node of the heap & rebuilds the heap"""
        poll = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        del self.heap[-1]
        self.heapify_down()
        return poll

    def add(self, item: int):
        """Adds a new item to the heap"""
        self.heap.append(item)
        self.heapify_up()

    def heapify_up(self):
        """Bubbles the last item up the heap"""
        index = len(self.heap) - 1
        while self.__has_parent(index) and self.__get_parent(index) > self.heap[index]:
            self.__swap(self.__get_parent_index(index), index)
            index = self.__get_parent_index(index)

    def heapify_down(self):
        """Bubbles the parent down the heap as far as possible"""
        index = 0
        while self.__has_left_child(index):
            smaller_child_index = self.__get_left_child_index(index)
            if self.__has_right_child(index) and self.__get_right_child(
                index
            ) < self.__get_left_child(index):
                smaller_child_index = self.__get_right_child_index(index)

            if self.heap[index] < self.heap[smaller_child_index]:
                return

            self.__swap(index, smaller_child_index)
            index = smaller_child_index


def main():
    """HeapSort algorithm using MinHeap"""
    array = [54, 1, 3, 2, 5, 4, 8, 65, 47]
    heap = MinHeap(array)
    sorted_array = []

    for _ in range(0, len(array)):
        value = heap.poll()
        sorted_array.append(value)

    print(array)
    print(sorted_array)


if __name__ == "__main__":
    main()
