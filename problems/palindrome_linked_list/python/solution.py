""" Palindrome Linked List """


class ListNode:
    """
    Represents a singly-linked list node
    """

    def __init__(self, value, next=None) -> None:
        self.value = value
        self.next = next


def reverse(node: ListNode) -> ListNode:
    """
    Reverses a ListNode
    """
    if node is None:
        return node

    prev = None
    current = node
    while current is not None:
        tmp = current.next
        current.next = prev
        prev = current
        current = tmp

    return prev


def is_palindrome(head: ListNode) -> bool:
    """
    Determines if a linked list is a palindrome
    """
    slow = head
    fast = head

    while fast is not None:
        if fast.next is None:
            break
        slow = slow.next
        fast = fast.next.next

    back_half = reverse(slow)
    current = head

    while back_half is not None:
        if current.value != back_half.value:
            return False
        back_half = back_half.next
        current = current.next

    return True


def main():
    """
    Entrypoint
    """
    head = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))
    print(is_palindrome(head))


if __name__ == "__main__":
    main()
