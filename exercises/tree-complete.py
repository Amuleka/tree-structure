class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def in_order_traversal(self):
        if self is None:
            return []

        left_values = []
        if self.left:
            left_values = self.left.in_order_traversal()

        root_value = [self.value]

        right_values = []
        if self.right:
            right_values = self.right.in_order_traversal()

        return left_values + root_value + right_values


# Test Case 1:
#       4
#      / \
#     2   6
#    / \ 
#   1   3
root1 = Node(4)
root1.left = Node(2)
root1.right = Node(6)
root1.left.left = Node(1)
root1.left.right = Node(3)
print(root1.in_order_traversal())  # Expected output: [1, 2, 3, 4, 6]

# Test Case 2:
#       1
#        \
#         2
#          \
#           3
root2 = Node(1)
root2.right = Node(2)
root2.right.right = Node(3)
print(root2.in_order_traversal())  # Expected output: [1, 2, 3]

# Test Case 3: Empty tree
root3 = None
if root3 is not None:
    print(root3.in_order_traversal())
else:
    print([])  # Expected output: []

# Test Case 4:
#       5
#      /
#     3
#    / \
#   2   4
root4 = Node(5)
root4.left = Node(3)
root4.left.left = Node(2)
root4.left.right = Node(4)
print(root4.in_order_traversal())  # Expected output: [2, 3, 4, 5]
