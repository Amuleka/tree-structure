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

## Exercise

In this exercise, we will create a binary search tree (BST) and perform various operations on it.

1. Define the `Node` class to represent nodes in the BST. Each node should have a `value`, `left` child, and `right` child.

2. Define the `insert` function to insert values into the BST while maintaining the BST property. The function should take the current `root` node and the `value` to be inserted. If the `root` is `None`, create a new node with the given value. Otherwise, recursively call the `insert` function on the left or right child, depending on the value.

3. Define the `in_order_traversal` function to perform an in-order traversal of the BST. This function should return a list of values in sorted order. The algorithm for in-order traversal is as follows:

   - If the root is `None`, return an empty list.
   - Recursively traverse the left subtree using the `in_order_traversal` function and assign the result to `left_values`.
   - Create a list containing the value of the root node and assign it to `root_value`.
   - Recursively traverse the right subtree using the `in_order_traversal` function and assign the result to `right_values`.
   - Concatenate `left_values`, `root_value`, and `right_values` to obtain the final result.

4. Create an empty BST by initializing the `root` variable as `None`.

5. Insert the following values into the BST: `[8, 3, 10, 1, 6, 14, 4, 7, 13]` using the `insert` function.

6. Perform an in-order traversal of the BST using the `in_order_traversal` function and print the result.

The expected output is `[1, 3, 4, 6, 7, 8, 10, 13, 14]`, which represents the sorted values of the BST.

# Practice

It is time to test your knowledge. Click on [this link](https://github.com/Amuleka/tree-structure/blob/main/exercises/tree-incomplete.py) to do the exercise.

Once you've done it or tried it for a couple of times you can check the solution [here](https://github.com/Amuleka/tree-structure/blob/main/exercises/tree-complete.py).
