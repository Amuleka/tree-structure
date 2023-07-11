# Tree

# Introduction to Trees

A tree is a hierarchical data structure that consists of nodes connected by edges. It starts with a root node and has child nodes branching out from the root. Each node can have multiple children, forming a branching structure. Trees are used to represent hierarchical relationships between data.

# Binary Trees: Definition and Properties

A binary tree is a type of tree where each node has at most two children, referred to as the left child and the right child. The properties of a binary tree include:

    Each node can have a maximum of two children.
    The left child is typically smaller than the parent, and the right child is larger.

# Binary Search Trees: Definition and Operations

A binary search tree (BST) is a special type of binary tree where the values of all nodes in the left subtree are less than the value of the parent node, and the values of all nodes in the right subtree are greater. BST supports the following operations:

    Insertion: Adding a new node to the tree while maintaining the BST property.
    Deletion: Removing a node from the tree while maintaining the BST property.
    Search: Finding a specific value in the tree efficiently.

# Tree Traversal Algorithms

Tree traversal refers to the process of visiting each node in a tree in a specific order. The commonly used traversal algorithms are:

    Pre-order traversal: Visit the root node first, followed by the left subtree, and then the right subtree.
    In-order traversal: Visit the left subtree first, then the root node, and finally the right subtree.
    Post-order traversal: Visit the left subtree first, then the right subtree, and finally the root node.

# Balanced Trees

Balanced trees are tree structures designed to ensure that the height of the tree remains balanced, optimizing search and insertion operations. Two commonly used balanced trees are:

    AVL Trees: Self-balancing binary search trees where the heights of the left and right subtrees differ by at most one.
    Red-Black Trees: Self-balancing binary search trees that maintain balance using color properties on the nodes.

# Tree Applications

Trees find applications in various domains, including:

    Expression evaluation: Trees can be used to represent and evaluate mathematical expressions.
    File systems: File systems often use tree structures to represent directories and files, enabling efficient navigation and organization.

## Exercise

Let's create a binary search tree (BST) and perform some operations on it.

```python
# Binary Search Tree (BST) Node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Insertion operation for BST
def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)

    return root

# In-order traversal for BST
def in_order_traversal(root):
    if root is None:
        return []

    left_values = in_order_traversal(root.left)
    root_value = [root.value]
    right_values = in_order_traversal(root.right)

    return left_values + root_value + right_values

# Create a BST
root = None

# Insert values into the BST
values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for value in values:
    root = insert(root, value)

# Perform in-order traversal
print(in_order_traversal(root))  # Expected output: [1, 3, 4, 6, 7, 8, 10, 13, 14]
```

Sure! Here's the exercise formatted using markup language:

markdown

## Exercise

Let's create a binary search tree (BST) and perform some operations on it.

```python
# Binary Search Tree (BST) Node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Insertion operation for BST
def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)

    return root

# In-order traversal for BST
def in_order_traversal(root):
    if root is None:
        return []

    left_values = in_order_traversal(root.left)
    root_value = [root.value]
    right_values = in_order_traversal(root.right)

    return left_values + root_value + right_values

# Create a BST
root = None

# Insert values into the BST
values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for value in values:
    root = insert(root, value)

# Perform in-order traversal
print(in_order_traversal(root))  # Expected output: [1, 3, 4, 6, 7, 8, 10, 13, 14]

In this exercise, we define the Node class to represent nodes in a binary search tree (BST). We also define the insert function to insert values into the BST while maintaining the BST property. The in_order_traversal function performs an in-order traversal of the BST and returns the values in sorted order.

We then create an empty BST, insert values [8, 3, 10, 1, 6, 14, 4, 7, 13] into it using the insert function, and finally perform an in-order traversal using the in_order_traversal function. The expected output is [1, 3, 4, 6, 7, 8, 10, 13, 14], which represents the sorted values of the BST.

In this exercise, we create a binary search tree (BST) and perform various operations on it.

    First, we define the Node class to represent nodes in the BST. Each node has a value, left child, and right child.
    Next, we define the insert function to insert values into the BST while maintaining the BST property. It takes the current root and the value to be inserted. If the root is None, a new node is created with the given value. Otherwise, the function recursively calls itself on the left or right child depending on the value.
    We also define the in_order_traversal function to perform an in-order traversal of the BST. It returns a list of values in sorted order. The function recursively traverses the left subtree, visits the root node, and then traverses the right subtree.
    Finally, we create an empty BST by initializing the root variable as None. We insert values [8, 3, 10, 1, 6, 14, 4, 7, 13] into the BST using the insert function. Finally, we perform an in-order traversal using the in_order_traversal function and print the result.

The expected output of the program is [1, 3, 4, 6, 7, 8, 10, 13, 14], which represents the sorted values of the BST.
```

# Practice
