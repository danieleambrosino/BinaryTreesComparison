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
        while node.left is not None:
            node = node.left
        return node.key

    def maximum(self, node=None):
        if node is None:
            node = self.root
        while node.right is not None:
            node = node.right
        return node.key

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

    def height(self):
        def _height(node):
            if node is None:
                return 0
            return max(_height(node.left), _height(node.right)) + 1
        return _height(self.root)


class RedBlackNode(Node):
    def __init__(self, key=None):
        Node.__init__(self, key)
        self.is_red = True


class RedBlackTree(BinarySearchTree):
    def __init__(self):
        BinarySearchTree.__init__(self)

        '''NIL special value'''
        self.nil = RedBlackNode()
        self.nil.is_red = False

        self.root = self.nil

    def insert(self, value):
        def fix_up(node):
            while node.parent.is_red:
                if node.parent is node.parent.parent.left:
                    uncle = node.parent.parent.right
                    if uncle.is_red:
                        node.parent.is_red = False
                        uncle.is_red = False
                        node.parent.parent.is_red = True
                        node = node.parent.parent
                    else:
                        if node is node.parent.right:
                            node = node.parent
                            self.left_rotate(node)
                        node.parent.is_red = False
                        node.parent.parent.is_red = True
                        self.right_rotate(node.parent.parent)
                else:
                    uncle = node.parent.parent.left
                    if uncle.is_red:
                        node.parent.is_red = False
                        uncle.is_red = False
                        node.parent.parent.is_red = True
                        node = node.parent.parent
                    else:
                        if node is node.parent.left:
                            node = node.parent
                            self.right_rotate(node)
                        node.parent.is_red = False
                        node.parent.parent.is_red = True
                        self.left_rotate(node.parent.parent)
            self.root.is_red = False

        node = RedBlackNode(value)
        previous = self.nil
        current = self.root

        '''Find correct position'''
        while current is not self.nil:
            previous = current
            if node.key < current.key:
                current = current.left
            else:
                current = current.right

        '''Insert value'''
        node.parent = previous
        if previous is self.nil:
            self.root = node
        elif node.key < previous.key:
            previous.left = node
        else:
            previous.right = node

        node.left = self.nil
        node.right = self.nil
        # node.is_red == True by default
        fix_up(node)

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left.key is not None:
            y.left.parent = x
        y.parent = x.parent
        if x.parent.key is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right.key is not None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent.key is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.right = x
        x.parent = y
