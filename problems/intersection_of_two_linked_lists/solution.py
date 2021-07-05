""" Intersection of Two Linked Lists """


class ListNode:
    """
    Represents a singly linked list node
    """

    def __init__(self, x):
        self.val = x
        self.next = None

    def items(self):
        items = [self.val]
        if self.next is not None:
            items.extend(self.next.items())
        return items


def length(head: ListNode):
    """
    Returns the length of a linked list
    """
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count


def get_intersection_node(headA: ListNode, headB: ListNode) -> ListNode:
    """
    Returns the intersection node of two singly linked lists, if there is one
    """
    len_a = length(headA)
    len_b = length(headB)

    if len_a > len_b:
        difference = len_a - len_b
        smaller = headB
        bigger = headA
    else:
        difference = len_b - len_a
        smaller = headA
        bigger = headB

    for _ in range(difference):
        if bigger == smaller:
            return bigger
        bigger = bigger.next

    while bigger is not None and smaller is not None:
        if bigger == smaller:
            return bigger
        bigger = bigger.next
        smaller = smaller.next

    return None


def create_test_case(before: list, intersection: ListNode, after: list):
    head = ListNode(before[0])
    pointer = head
    for i in range(1, len(before)):
        pointer.next = ListNode(before[i])
        pointer = pointer.next

    pointer.next = intersection
    pointer = pointer.next

    for i in after:
        pointer.next = ListNode(i)
        pointer = pointer.next

    return head


def main():
    """
    Entrypoint
    """
    intersections = [ListNode(8), ListNode(2), None]
    test_cases = [
        (([4, 1], intersections[0], [4, 5]), ([5, 6, 1], intersections[0], [4, 5])),
    ]

    for a, b in test_cases:
        a = create_test_case(a[0], a[1], a[2])
        b = create_test_case(b[0], b[1], b[2])
        intersection = get_intersection_node(a, b)
        if intersection is None:
            print("No intersection")
        else:
            print(intersection.val)


if __name__ == "__main__":
    main()
