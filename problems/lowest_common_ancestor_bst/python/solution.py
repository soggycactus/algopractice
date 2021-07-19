""" Lowest Common Ancestor of Binary Search Tree """


class TreeNode:
    """
    Represents a node in a Binary Search Tree
    """

    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def find_ancestors(root: TreeNode, target: TreeNode):
    """
    Finds all the ancestors of the target node in the BST
    """
    ancestors = []
    if root is None:
        return ancestors

    ancestors.append(root)
    if root == target:
        return ancestors

    if target.val > root.val:
        ancestors.extend(find_ancestors(root.right, target))
    else:
        ancestors.extend(find_ancestors(root.left, target))

    return ancestors


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Finds the lowest common ancestor of the two given tree nodes
    """
    q_ancestors = find_ancestors(root, q)
    p_ancestors = find_ancestors(root, p)

    for i in range(len(q_ancestors) - 1, -1, -1):
        if q_ancestors[i] in p_ancestors:
            return q_ancestors[i]


def main():
    """
    Entrypoint
    """

    root = TreeNode(
        6,
        TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
        TreeNode(8, TreeNode(7), TreeNode(9)),
    )

    test_cases = [
        (root.left, root.right),
        (root.left, root.left.right),
        (root.right.left, root.right.right),
        (root.left.right.left, root.left.right.right),
        (root.left.right, root.left.right.right),
        (root.left, root.right.right),
        (root, root.right.right),
    ]

    for p, q in test_cases:
        lca = lowest_common_ancestor(root, p, q)
        print(lca.val)


if __name__ == "__main__":
    main()
