""" Merge Two Sorted Linked Lists """


class ListNode:
    """
    Represents a singly linked list node
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        """
        Prints the linked list from this node onwards
        """
        print(self.val)
        if self.next is not None:
            self.next.print()


def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    """
    Merges two sorted singly linked lists
    """
    if l1 is None and l2 is None:
        return None
    if l1 is None and l2 is not None:
        return l2
    if l2 is None and l1 is not None:
        return l1

    if l1.val < l2.val:
        node = ListNode(l1.val)
        l1 = l1.next
    else:
        node = ListNode(l2.val)
        l2 = l2.next

    current = node
    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            current.next = ListNode(l1.val)
            current = current.next
            l1 = l1.next
        else:
            current.next = ListNode(l2.val)
            current = current.next
            l2 = l2.next

    if l1 is not None:
        current.next = l1

    if l2 is not None:
        current.next = l2

    return node


def main():
    """
    Entrypoint
    """
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    merged = merge_two_lists(l1, l2)
    merged.print()


if __name__ == "__main__":
    main()
