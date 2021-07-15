""" Same Binary Tree """


class TreeNode:
    """
    Represents a Binary Tree Node
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    """
    Determines whether a binary tree is the same
    """
    if p is None and q is None:
        return True
    elif p is None or q is None:
        return False
    elif p.val != q.val:
        return False
    else:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


def main():
    """
    Entrypoint
    """
    test_cases = [
        [TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))],
        [TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2))],
        [TreeNode(1, TreeNode(2), TreeNode(1)), TreeNode(1, TreeNode(1), TreeNode(2))],
    ]

    for p, q in test_cases:
        print(is_same_tree(p, q))


if __name__ == "__main__":
    main()
