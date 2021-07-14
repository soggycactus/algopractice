""" Insertion Sort Linked List """


class ListNode:
    """
    Represents a singly linked-list node
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def items(self):
        """
        Returns the items in the linked list from this node onwards
        """
        items = [self.val]
        if self.next is not None:
            items.extend(self.next.items())

        return items


def swap(p1: ListNode):
    """
    Swaps a node forward in linked list
    """
    tmp = p1.val
    p1.val = p1.next.val
    p1.next = ListNode(tmp, p1.next.next)


def insertion_sort_linked_list(head: ListNode) -> ListNode:
    """
    Performs insertion sort on singly linked list
    """
    # 4,2,1,3
    # 2,4,1,3
    # 2,1,4,3
    # 2,1,3,4
    # 1,2,3,4
    while True:
        pointer = head  # 4
        swapped = False
        while pointer is not None:
            if pointer.next is None:
                break
            if pointer.val > pointer.next.val:
                swap(pointer)  # 4 -> 2 -> 1 -> 3
                swapped = True
                pointer = pointer.next  # 4,1,3 -> 4,3 -> 4
            else:
                pointer = pointer.next
        if swapped is False:
            break
    return head


def create_linked_list(items: list):
    """
    Creates singly linked list from array of items
    """
    head = ListNode(items[0])
    pointer = head

    for i in range(1, len(items)):
        pointer.next = ListNode(items[i])
        pointer = pointer.next

    return head


def main():
    """
    Entrypoint
    """
    test_cases = [
        [4, 2, 1, 3],
        [-1, 5, 3, 4, 0],
        [
            1,
            4,
            2,
            5,
            7,
            8,
            5,
            2,
            2,
            8,
            5,
            4,
            6,
            3,
            9,
            7,
            5,
            2,
            1,
            89,
            12,
            5,
            7,
            8,
            4,
            5,
            58,
            4,
            1,
            5,
            5,
            7,
            4,
            5,
            6,
            3,
            21,
            5,
            8,
            4,
            5,
            9,
            6,
        ],
    ]

    for test in test_cases:
        head = create_linked_list(test)
        print(head.items())
        insertion_sort_linked_list(head)
        print(head.items())


if __name__ == "__main__":
    main()
