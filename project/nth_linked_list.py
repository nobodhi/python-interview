# find the nth element of a linked list

# Use this class to create linked lists.


class Node:
    def __init__(self, value, child=None):
        self.value = value
        self.child = child

    # The string representation of this node.
    # Will be used for testing.
    def __str__(self):
        return str(self.value)


# NOTE: Feel free to use the following function for testing.
# It converts the given linked list into an easy-to-read string format.
# Example: 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> (None)
def linked_list_to_string(head):
    current = head
    str_list = []
    while current:
        str_list.append(str(current.value))
        current = current.child
    str_list.append('(None)')
    return ' -> '.join(str_list)


#  ~~~~~~~~~~~~~~~~~~
# Implement your function below
#  ~~~~~~~~~~~~~~~~~~
def nth_from_last(head, n):
    """using two pointers a distance of n apart, locate the nth from end"""
    if head is None or type(head) is not Node or n is None or type(n) is not int or n < 0:
        print("None")
        return None
    tail_pointer = head
    nth_pointer = head
    for _ in range(n):
        if tail_pointer is None: # !
            return None
        tail_pointer = tail_pointer.child
    while tail_pointer:
        tail_pointer = tail_pointer.child
        nth_pointer = nth_pointer.child
    print(nth_pointer)
    return nth_pointer


# NOTE: The following input values will be used for testing your solution.
def run_tests():
    current = Node(1)
    for i in range(2, 8):
        current = Node(i, current)
    head = current
    # head = 7 -> 6 -> 5 -> 4 -> 3 -> 2 -> 1 -> (None)

    nth_from_last(head, 1)  # should return 1.
    nth_from_last(head, 5)  # should return 5.

    current = Node(4)
    for i in reversed(range(1, 4)):
        current = Node(i, current)
    head = current
    # head = 1 -> 2 -> 3 -> 4 -> (None)

    nth_from_last(head, 2)  # should return 3.
    nth_from_last(head, 4)  # should return 1.
    nth_from_last(head, 5)  # should return None.
    nth_from_last(None, 1)  # should return None.

    # 5 invalid inputs:
    # nth_from_last(head, 1.1)
    # nth_from_last(head, -1)
    # nth_from_last(None, -1)
    # nth_from_last("head", 1)
    # nth_from_last(head, "1")


run_tests()
