from avl_tree import build_tree, tree_to_str


def sum_values(root):
    """Return the sum of all keys in the tree (0 for an empty tree).

    Iterative DFS with an explicit stack visits every node once.
    Time: O(n), memory: O(h).
    """
    total = 0
    stack = [root] if root else []
    while stack:
        node = stack.pop()
        total += node.key
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return total


if __name__ == "__main__":
    keys = [10, 20, 30, 25, 28, 27, -1, 5, 15]
    root = build_tree(keys)

    print("AVL tree:")
    print(tree_to_str(root))
    print(f"Sum of all values: {sum_values(root)}")

    assert sum_values(root) == sum(keys)
    assert sum_values(None) == 0
