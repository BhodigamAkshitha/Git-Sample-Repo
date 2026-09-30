"""Simple Binary Search Tree implementation with demo.

This module provides `Node` and `BinarySearchTree` classes for
insertion, search, traversal and deletion operations. Run the file
directly to see a small demo.
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.key})"


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a key
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    # Search for a key
    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    # Inorder traversal (sorted order)
    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    # Delete a key
    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # Node with one or no child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            # Node with two children: inorder successor
            successor = self._min_value_node(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current


if __name__ == "__main__":
    # Demo usage: build a BST, show inorder, search, delete
    bst = BinarySearchTree()
    for v in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(v)

    print("Inorder:", bst.inorder())
    print("Search 60:", bst.search(60))
    print("Search 25:", bst.search(25))

    bst.delete(70)
    print("After deleting 70:", bst.inorder())
