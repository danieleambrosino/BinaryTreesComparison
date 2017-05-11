class Node:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def ordered_walk(self):
        def _ordered_walk(node):
            if node is None:
                return
            if node.left is not None:
                _ordered_walk(node.left)
            print node.key
            if node.right is not None:
                _ordered_walk(node.right)

        _ordered_walk(self.root)

    def search(self, value):
        node = self.root
        while node is not None and value != node.key:
            if value < node.key:
                node = node.left
            else:
                node = node.right
        return node

    def minimum(self, node=None):
        if node is None:
            node = self.root
        while node is not None:
            node = node.left
        return node

    def maximum(self, node=None):
        if node is None:
            node = self.root
        while node is not None:
            node = node.right
        return node

    def successor(self, node=None):
        if node is None:
            node = self.root
        if node.right is not None:
            return self.minimum(node.right)
        successor = node.parent
        while successor is not None and node == successor.right:
            node = successor
            successor = successor.parent
        return successor

    def predecessor(self, node=None):
        if node is None:
            node = self.root
        if node.left is not None:
            return self.maximum(node.left)
        predecessor = node.parent
        while predecessor is not None and node == predecessor.left:
            node = predecessor
            predecessor = predecessor.parent
        return predecessor

    def insert(self, value):
        node = Node(value)
        parent = None
        current = self.root
        while current is not None:
            parent = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right
        node.parent = parent
        if parent is None:
            self.root = node
        elif node.key < parent.key:
            parent.left = node
        else:
            parent.right = node
