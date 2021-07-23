""" Binary Tree Pruning """


class TreeNode:
    """
    Represents a Binary Tree Node
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def inorder_traversal(self) -> list:
        items = []

        if self.left is not None:
            items.extend(self.left.inorder_traversal())
        items.append(self.val)
        if self.right is not None:
            items.extend(self.right.inorder_traversal())
        return items


def has_one(node: TreeNode) -> bool:
    """
    Returns whether a Binary Tree has 1 somewhere along its tree
    """
    if node.val == 1:
        return True
    else:
        if node.left is None and node.right is None:
            return False
        if node.left is not None and node.right is None:
            return has_one(node.left)
        if node.right is not None and node.left is None:
            return has_one(node.right)
        else:
            return has_one(node.left) or has_one(node.right)


def prune_tree(root: TreeNode) -> TreeNode:
    """
    Prunes a Binary Tree of all subtrees that do not have 1
    """
    if root.right is not None:
        if has_one(root.right) is False:
            root.right = None
        else:
            root.right = prune_tree(root.right)

    if root.left is not None:
        if has_one(root.left) is False:
            root.left = None
        else:
            root.left = prune_tree(root.left)

    if root.left is None and root.right is None:
        if root.val != 1:
            return None

    return root


def main():
    """
    Entrypoint
    """
    root = TreeNode(
        1,
        TreeNode(1, TreeNode(1, TreeNode(0)), TreeNode(1)),
        TreeNode(0, TreeNode(0), TreeNode(1)),
    )

    print(root.inorder_traversal())
    root = prune_tree(root)
    print(root.inorder_traversal())


if __name__ == "__main__":
    main()
