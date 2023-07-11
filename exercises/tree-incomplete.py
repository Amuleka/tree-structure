'''
Your task is to complete the function in_order_traversal() that performs an in-order traversal of a binary tree and returns a list of values representing the order of visited nodes. 
The in-order traversal visits the left subtree, then the root node, and finally the right subtree.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def in_order_traversal(node):
        # Incomplete implementation
        # Your task is to complete this function
        pass  # Remove this line and complete the function

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
print(in_order_traversal(root1))  # Expected output: [1, 2, 3, 4, 6]

# Test Case 2:
#       1
#        \
#         2
#          \
#           3
root2 = Node(1)
root2.right = Node(2)
root2.right.right = Node(3)
print(in_order_traversal(root2))  # Expected output: [1, 2, 3]

# Test Case 3: Empty tree
root3 = None
print(in_order_traversal(root3))  # Expected output: []

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
print(in_order_traversal(root4))  # Expected output: [2, 3, 4, 5]
