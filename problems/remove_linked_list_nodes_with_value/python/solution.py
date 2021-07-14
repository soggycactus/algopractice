""" Remove Nodes from a Linked List with a specific value"""


class ListNode:
    """
    Represents a node in a singly linked list
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        current = self
        result = []
        while current is not None:
            result.append(current.val)
            current = current.next
        print(result)


def remove_elements(head: ListNode, val: int) -> ListNode:
    """
    Removes all nodes with given value from a singly linked list
    """
    if head is None:
        return head

    current = head
    while True:
        if current is None:
            return head
        elif current.val != val:
            break
        else:
            head = current.next
            current = head

    while current.next is not None:
        if current.next.val == val:
            while current.next.val == val:
                current.next = current.next.next
                if current.next is None:
                    break
        if current.next is None:
            break
        current = current.next

    return head


def main():
    """
    Entrypoint
    """
    test_cases = [
        (ListNode(1, ListNode(2, ListNode(2, ListNode(1)))), 2),
        (
            ListNode(
                1,
                ListNode(
                    2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))
                ),
            ),
            6,
        ),
        (
            ListNode(7, ListNode(7, ListNode(7, ListNode(7)))),
            7,
        ),
    ]

    for i, j in test_cases:
        print("running test case - removing", j)
        i.print()
        i = remove_elements(i, j)
        if i is None:
            print([])
        else:
            i.print()


if __name__ == "__main__":
    main()
