""" Binary Tree Inorder Traversal """


class TreeNode:
    """
    Represents a Binary Tree Node
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode):
    """
    Performs inorder traversal of a binary tree
    """
    if root is None:
        return []

    items = []
    if root.left is not None:
        items.extend(inorder_traversal(root.left))
    items.append(root.val)
    if root.right is not None:
        items.extend(inorder_traversal(root.right))

    return items


def create_binary_tree(items: list) -> TreeNode:
    """
    Creates a binary tree from an array
    """
    node = TreeNode(items[0])
    pointer = node
    left = True
    count = 0
    for i in range(1, len(items)):
        if count == 2:
            pointer = pointer.right
        if left is True:
            node.left = TreeNode(items[i])
            left = False
        else:
            node.right = TreeNode(items[i])
            left = True
        count += 1

    return node


def main():
    """
    Entrypoint
    """
    test_cases = [
        TreeNode(1, None, TreeNode(2, TreeNode(3))),
        TreeNode(1, TreeNode(2)),
        TreeNode(1, None, TreeNode(2)),
    ]
    for test in test_cases:
        print(inorder_traversal(test))


if __name__ == "__main__":
    main()
