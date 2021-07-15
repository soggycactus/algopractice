""" Symmetric Binary Tree """


class TreeNode:
    """
    Represents a Binary Tree Node
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal_with_nulls(root: TreeNode):
    """
    Performs inorder traversal of a binary tree including null values
    """
    items = []
    if root.left is None and root.right is None:
        items.append(root.val)
        return items

    if root.left is not None:
        items.extend(inorder_traversal_with_nulls(root.left))
    else:
        items.append(None)
    items.append(root.val)
    if root.right is not None:
        items.extend(inorder_traversal_with_nulls(root.right))
    else:
        items.append(None)

    return items


def reverse_order_traversal_with_nulls(root: TreeNode):
    """
    Performs postorder traversal of a binary tree with null values
    """
    items = []
    if root.left is None and root.right is None:
        items.append(root.val)
        return items

    if root.right is not None:
        items.extend(reverse_order_traversal_with_nulls(root.right))
    else:
        items.append(None)
    items.append(root.val)
    if root.left is not None:
        items.extend(reverse_order_traversal_with_nulls(root.left))
    else:
        items.append(None)

    return items


def is_symmetric(root: TreeNode) -> bool:
    """
    Returns whether a binary tree is symmetric
    """
    if root.left is None and root.right is None:
        return True
    if root.left is None or root.right is None:
        return False
    if root.left.val != root.right.val:
        return False
    return reverse_order_traversal_with_nulls(root) == inorder_traversal_with_nulls(
        root
    )


def main():
    """
    Entrypoint
    """
    test_cases = [
        TreeNode(
            2,
            TreeNode(3, TreeNode(4), TreeNode(5, TreeNode(8), TreeNode(9))),
            TreeNode(3, TreeNode(5, TreeNode(9), TreeNode(8)), TreeNode(4)),
        ),
        TreeNode(1, TreeNode(2, TreeNode(2)), TreeNode(2, TreeNode(2))),
    ]

    for test in test_cases:
        print(is_symmetric(test))


if __name__ == "__main__":
    main()
