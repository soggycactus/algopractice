""" Valid Binary Search Tree """


class TreeNode:
    """
    Represents a BST Node
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_bst_children(root: TreeNode) -> list:
    """
    Returns all of the children of a BST
    """
    children = []
    if root.left is None and root.right is None:
        return children
    elif root.left is None and root.right is not None:
        children.append(root.right.val)
        children.extend(get_bst_children(root.right))
    elif root.right is None and root.left is not None:
        children.append(root.left.val)
        children.extend(get_bst_children(root.left))
    else:
        children.append(root.left.val)
        children.append(root.right.val)
        children.extend(get_bst_children(root.left))
        children.extend(get_bst_children(root.right))

    return children


def is_valid_bst(root: TreeNode) -> bool:
    """
    Determines if a BST is valid
    """
    if root.left is None and root.right is None:
        return True
    elif root.left is None and root.right is not None:
        if root.val < root.right.val and is_valid_bst(root.right):
            right_children = get_bst_children(root.right)
            if right_children != []:
                return root.val < min(right_children)
            return True
        return False
    elif root.right is None and root.left is not None:
        if root.left.val < root.val and is_valid_bst(root.left):
            left_children = get_bst_children(root.left)
            if left_children != []:
                return root.val > max(left_children)
            return True
        return False
    else:
        if (
            root.left.val < root.val < root.right.val
            and is_valid_bst(root.left)
            and is_valid_bst(root.right)
        ):
            right_children = get_bst_children(root.right)
            if right_children != []:
                if not root.val < min(right_children):
                    return False

                left_children = get_bst_children(root.left)
                if left_children != []:
                    return root.val > max(left_children)

                return True
            else:
                left_children = get_bst_children(root.left)
                if left_children != []:
                    return root.val > max(left_children)
                return True
        return False


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
    ]

    for bst, result in test_cases:
        print(bst.val, get_bst_children(bst))
        print(is_valid_bst(bst) == result)


if __name__ == "__main__":
    main()
