
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def _insert(self, node, key):
        if node is None:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _print_parents(self, node, parent):
        if node:
            if parent is None:
                print(node.key, "-> Root")
            else:
                print(node.key, "-> ", parent.key)

            self._print_parents(node.left, node)
            self._print_parents(node.right, node)

    def print_parents(self):
        print("Parents are: ")
        self._print_parents(self.root, None)

# ზედმეტი რაც იყო წავშალე

    def _print_leaves(self, node):
        if node:
            if node.left is None and node.right is None:
                print(node.key)
            self._print_leaves(node.left)
            self._print_leaves(node.right)
    
    def print_leaves(self):
        print("leaf nodes: ")
        self._print_leaves(self.root)
        print()


bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(9)
bst.insert(6)
bst.insert(12)
bst.insert(10)
bst.insert(11)

bst.print_parents()
bst.print_leaves()














