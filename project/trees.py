class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BTree():
    def __init__(self, value):
        self.root = Node(value)

    def pre_order(self, n, visited=[]):
        visited.append(n.value)
        if n.left:
            self.pre_order(n.left)
        if n.right:
            self.pre_order(n.right)
        return visited


t = BTree(1)
t.root.left = Node(2)
t.root.right = Node(3)
t.root.left.left = Node(4)
t.root.left.right = Node(5)
t.root.right.left = Node(6)
t.root.right.right = Node(7)
print(t.pre_order(t.root))
