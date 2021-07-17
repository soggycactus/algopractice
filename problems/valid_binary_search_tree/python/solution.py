""" Valid Binary Search Tree """


class TreeNode:
    """
    Represents a BST Node
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(root: TreeNode) -> list:
    """
    Performs inorder traversal of a binary tree
    """
    if root is None:
        return []

    items = []

    items.extend(inorder_traversal(root.left))
    items.append(root.val)
    items.extend(inorder_traversal(root.right))

    return items


def is_valid_bst(root: TreeNode) -> bool:
    """
    Determines if a BST is valid
    """
    inorder = inorder_traversal(root)

    for i in range(1, len(inorder)):
        if inorder[i - 1] >= inorder[i]:
            return False

    return True


def main():
    """
    Entrypoint
    """
    test_cases = [
        (TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7))), False),
        (TreeNode(2, TreeNode(1), TreeNode(3)), True),
        (TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))), False),
        (
            TreeNode(
                3,
                TreeNode(1, TreeNode(0), TreeNode(2)),
                TreeNode(5, TreeNode(4), TreeNode(6)),
            ),
            True,
        ),
        (
            TreeNode(
                32,
                TreeNode(26, TreeNode(19, None, TreeNode(27)), None),
                TreeNode(47, None, TreeNode(56)),
            ),
            False,
        ),
        (TreeNode(2, TreeNode(2), TreeNode(2)), False),
        (TreeNode(0, TreeNode(-1)), True),
    ]

    for bst, result in test_cases:
        print(inorder_traversal(bst))
        print(is_valid_bst(bst) == result)


if __name__ == "__main__":
    main()
