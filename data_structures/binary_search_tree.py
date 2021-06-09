""" Binary Search Tree """


class BinarySearchTreeNode:
    """
    BinarySearchTreeNode implements a BST
    """

    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def insert(self, data: int) -> None:
        """
        Inserts a new element into the BST
        """
        if data <= self.data:
            if self.left is None:
                self.left = BinarySearchTreeNode(data)
                self.left.parent = self
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = BinarySearchTreeNode(data)
                self.right.parent = self
            else:
                self.right.insert(data)

    def inorder_tree_walk(self):
        """
        Performs an inorder tree walk
        """
        if self.left is not None:
            self.left.inorder_tree_walk()
        print(self.data)
        if self.right is not None:
            self.right.inorder_tree_walk()

    def find(self, value: int):
        """
        Searches the BST for a value
        """
        while self.data != value:
            if value < self.data and self.left is not None:
                return self.left.find(value)
            elif value > self.data and self.right is not None:
                return self.right.find(value)
            else:
                return None

        return self

    def min(self):
        """
        Returns the minumum element of the BST
        """
        x = self
        while x.left is not None:
            x = x.left
        return x.data

    def max(self):
        """
        Returns the maximum element of the BST
        """
        x = self
        while x.right is not None:
            x = x.right
        return x.data


def tree_minimum(node: BinarySearchTreeNode):
    """
    Returns the minimum element of a BST
    """
    while node.left is not None:
        node = node.left
    return node


def tree_maximum(node: BinarySearchTreeNode):
    """
    Returns the maximum element of a BST
    """
    while node.right is not None:
        node = node.right
    return node


def find_successor(node: BinarySearchTreeNode):
    """
    Returns the successor of a given BST node
    """
    if node.right is not None:
        return tree_minimum(node.right)

    parent = node.parent
    while parent is not None and parent.right == node:
        node = parent
        parent = node.parent

    return parent


def find_predecessor(node: BinarySearchTreeNode):
    """
    Returns the predecessor of a given BST node
    """
    if node.left is not None:
        return tree_maximum(node.left)

    parent = node.parent
    while parent is not None and parent.left == node:
        node = parent
        parent = node.parent

    return parent


def transplant(
    node: BinarySearchTreeNode, u: BinarySearchTreeNode, v: BinarySearchTreeNode
):
    """
    Replaces the subtree rooted at node `u` with the subtree rooted at node`v`
    """
    if u.parent is None:
        node.data = u.data
        node.right = u.right
        node.left = u.left
        node.parent = u.parent
    elif u == u.parent.left:
        u.parent.left = v
    else:
        u.parent.right = v

    if v is not None:
        v.parent = u.parent


def tree_delete(node: BinarySearchTreeNode, z: BinarySearchTreeNode):
    """
    Deletes node `z` from the BST
    """
    if z.left is None:
        transplant(node, z, z.right)
    elif z.right is None:
        transplant(node, z, z.left)
    else:
        y = tree_minimum(z.right)
        if y.parent != z:
            transplant(node, y, y.right)
            y.right = z.right
            y.right.parent = y
        transplant(node, z, y)
        y.left = z.left
        y.left.parent = y


def main():
    """
    Example Usage
    """
    bst = BinarySearchTreeNode(15)
    bst.insert(6)
    bst.insert(18)
    bst.insert(3)
    bst.insert(7)
    bst.insert(17)
    bst.insert(20)
    bst.insert(2)
    bst.insert(4)
    bst.insert(13)
    bst.insert(9)

    print("--- Inorder Tree Walk ---")
    bst.inorder_tree_walk()
    print("--- Find Element ---")
    find = bst.find(13)
    print(find.data)
    print("--- Maximum ---")
    print(bst.max())
    print("--- Minimum ---")
    print(bst.min())

    print("--- Successor ---")
    successor = find_successor(find)
    print(successor.data)

    print("--- Predecessor ---")
    predecessor = find_predecessor(find)
    print(predecessor.data)

    print("--- Delete 13 from BST ---")
    tree_delete(bst, find)
    bst.inorder_tree_walk()


if __name__ == "__main__":
    main()
