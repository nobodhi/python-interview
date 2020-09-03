# determine if a given tree is a BST

# Use this class to create binary trees.


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)


# NOTE:
# we shouldn't assume we're given a complete BST, i.e. with all non-leaf levels filled.
# to handle any BST, we must check the size of the child list or handle an exception.
def create_tree(mapping: dict, head_value: int) -> Node:
    """A function for creating a tree.
    Input:
    - mapping (dict): a node-to-node mapping that shows how the tree should be constructed
    - head_value (int): the value that will be used for the head node
    Output (Node):The head node of the resulting tree"""
    
    head = Node(head_value) # first node in the mapping: list(mapping.keys())[0]
    _tree = {head_value: head}  # private dict {int: Node}
    # NOTE we can do this in one pass if we maintain insertion order (default in 3.7)
    for key, value in mapping.items():
        if len(value) >= 1:
            _tree[value[0]] = Node(value[0])
        if len(value) >= 2:
            _tree[value[1]] = Node(value[1])
    for key, value in mapping.items():
        if len(value) >= 1:
            _tree[key].left = _tree[value[0]]
        if len(value) >= 2:
            _tree[key].right = _tree[value[1]]
    return head


# help(create_tree)

# The mapping we're going to use for constructing a tree.
# {0: [1, 2]} means that 0's left child is 1, and its right
# child is 2.
mapping1 = {0: [1, 2], 1: [3, 4], 2: [5, 6]}
mapping2 = {3: [1, 4], 1: [0, 2], 4: [5, 6]}
mapping3 = {3: [1, 5], 1: [0, 2], 5: [4, 6]}
mapping4 = {3: [1, 5], 1: [0, 4]}
mapping5 = {3: [1]}


# NOTE: The following values will be used for testing your solution.

head1 = create_tree(mapping1, 0)
# This tree is:
#  head1 = 0
#        /   \
#       1     2
#      /\    / \
#     3  4  5   6
head2 = create_tree(mapping2, 3)
# This tree is:
#  head2 = 3
#        /   \
#       1     4
#      /\    / \
#     0  2  5   6
head3 = create_tree(mapping3, 3)
# This tree is:
#  head3 = 3
#        /   \
#       1     5
#      /\    / \
#     0  2  4   6
head4 = create_tree(mapping4, 3)
# This tree is:
#  head4 = 3
#        /   \
#       1     5
#      /\
#     0  4

# NOTE we cannot assume a BST always has an odd number of nodes:
head5 = create_tree(mapping5, 3)
# This tree is:
#  head5 = 3
#        /
#       1


# Implement your function below.
def is_bst(node, lower_lim=None, upper_lim=None):
    # node is the top of the current sub-tree
    # print(node, node.left, node.right)
    if lower_lim is not None and node.value < lower_lim:
        return False
    if upper_lim is not None and node.value > upper_lim:
        return False
    result = True
    if node.left:
        if node.left.value < node.value:
            result = is_bst(node.left, lower_lim=lower_lim, upper_lim=node.value)
        else:
            result = False
    if result and node.right:
        if node.right.value > node.value:
            result = is_bst(node.right, lower_lim=node.value, upper_lim=upper_lim)
        else:
            result = False
    return result


print(is_bst(head5)) # length = 2, should return True
print(is_bst(head1)) # should return False
print(is_bst(head2)) # should return False
print(is_bst(head3)) # should return True
print(is_bst(head4))  # should return False

# better example: this is a violation because 25 is greater than 10 
#  head6 = 30
#        /   \
#       10     50
#      /\     /  \
#     5  20  35  60
#    / \
#   4  25

mapping6 = {30: [10, 50], 10: [5, 20], 5: [4, 25], 50: [35, 60]}
head6 = create_tree(mapping6, 30)
print(is_bst(head6))  # should return False

# moving left set an upper limit
# check the upper limit when moving right

# moving right set a lower limit
# check the lower limit when moving left
