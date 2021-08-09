""" Binary Tree Preorder Traversal """
from typing import List, Optional


class TreeNode:
    """
    Represents a Binary Tree node
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    """
    Returns the Preorder Traversal of a Binary Tree
    """
    if root is None:
        return []

    items = []

    items.append(root.val)

    items.extend(preorder_traversal(root.left))
    items.extend(preorder_traversal(root.right))

    return items


def main():
    """
    Entrypoint
    """
    test = TreeNode(1, None, TreeNode(2, TreeNode(3)))
    print(preorder_traversal(test))


if __name__ == "__main__":
    main()
