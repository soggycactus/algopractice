""" Linked List """


class LinkedListNode:
    """
    Represents a doubly linked list
    """

    def __init__(self, value, prevNode=None, nextNode=None) -> None:
        self.value = value
        self.prev = prevNode
        self.next = nextNode

    def print(self):
        """
        Prints the LinkedList from head to tail
        """
        head = self
        while head.prev is not None:
            head = head.prev

        while head is not None:
            print(head.value)
            head = head.next

    def head(self):
        """
        Returns the head of the current LinkedList
        """
        head = self
        while head.prev is not None:
            head = head.prev

        return head


def search(node: LinkedListNode, value) -> LinkedListNode:
    """
    Searches for a node in a LinkedList
    """
    x = node.head()
    while x is not None and x.value != value:
        x = x.next
    return x


def insert_head(l: LinkedListNode, node: LinkedListNode):
    """
    Inserts a new value at the beginning a LinkedList
    """
    while node.next is not None:
        node = node.next

    head = l.head()

    node.next = head
    node.prev = None
    head.prev = node


def insert_tail(l: LinkedListNode, node: LinkedListNode):
    """
    Inserts a new value at the end of a LinkedList
    """
    while True:
        if l.next is None:
            break
        l = l.next

    l.next = node
    node.prev = l


def delete(l: LinkedListNode, node: LinkedListNode):
    """
    Deletes a node from a LinkedList
    """
    if node.prev is not None:
        node.prev.next = node.next
    else:
        l.head = node.next
    if node.next is not None:
        node.next.prev = node.prev


def main():
    """
    Example Usage
    """
    ll = LinkedListNode(1)
    insert_head(ll, LinkedListNode(2))
    insert_head(ll, LinkedListNode(3))

    print("head insert")
    ll.print()

    insert_tail(ll, LinkedListNode(4))
    insert_tail(ll, LinkedListNode(5))

    print("tail insert")
    ll.print()

    print("Find 4")
    find = search(ll, 4)

    print("delete 4")
    delete(ll, find)
    ll.print()


if __name__ == "__main__":
    main()
