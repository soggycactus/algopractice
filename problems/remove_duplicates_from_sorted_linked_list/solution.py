""" Remove Duplicates from Sorted Linked List """


class ListNode:
    """
    Represents a node of a singly-linked list
    """

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def items(self):
        """
        Returns all items in the linked list from this node onwards
        """
        items = [self.val]
        next_node = self.next
        while next_node is not None:
            items.append(next_node.val)
            next_node = next_node.next
        return items


def delete_duplicates(head: ListNode) -> ListNode:
    """
    Deletes the duplicates of a sorted singly-linked list
    """
    if head is None:
        return head
    previous = head
    current = head.next
    while current is not None:
        if current.val == previous.val:
            previous.next = current.next
            current = current.next
        else:
            previous = current
            current = current.next

    return head


def create_test_case(items: list) -> ListNode:
    """
    Returns the head of the linked list for a test case
    """
    head = ListNode(items[0])
    current = head
    for i in range(1, len(items)):
        current.next = ListNode(items[i])
        current = current.next

    return head


def main():
    """
    Entrypoint
    """
    test_cases = [
        [1, 1, 2],
        [1, 1, 2, 3, 3],
        [4, 5, 6, 6, 7, 8, 9, 9],
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
    ]
    for test in test_cases:
        node = create_test_case(test)
        print("before: ", node.items())
        delete_duplicates(node)
        print("after: ", node.items())


if __name__ == "__main__":
    main()
