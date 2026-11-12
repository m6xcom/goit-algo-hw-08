from avl_tree import build_tree, tree_to_str


def find_min(root):
    """Return the smallest key in the tree, or None for an empty tree.

    In a BST the minimum is the leftmost node, so we walk left
    until there is no left child. Time: O(h), for AVL h = O(log n).
    """
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current.key


if __name__ == "__main__":
    keys = [10, 20, 30, 25, 28, 27, -1, 5, 15]
    root = build_tree(keys)

    print("AVL tree:")
    print(tree_to_str(root))
    print(f"Minimum value: {find_min(root)}")

    assert find_min(root) == min(keys)
    assert find_min(None) is None
