# Tree

# Introduction to trees

In computer science, a tree is a hierarchical data structure that consists of nodes connected by edges. Each node can have zero or more child nodes, except for the root node, which has no parent. Trees are commonly used to represent hierarchical relationships between data.

# Binary trees: definition and properties

A binary tree is a type of tree where each node can have at most two child nodes, commonly referred to as the left child and the right child. The properties of a binary tree include:

- Each node can have at most two child nodes.
- The left child node is smaller (or equal) in value compared to its parent node, and the right child node is greater in value.
- The order of insertion of nodes determines the structure of the binary tree.

# Binary search trees: definition and operations (insertion, deletion, search)

A binary search tree (BST) is a type of binary tree that maintains the property of the binary tree while also supporting efficient searching, insertion, and deletion operations. The operations on a binary search tree include:

- Insertion: Inserts a new node into the binary search tree while maintaining the binary search tree property.
- Deletion: Removes a node from the binary search tree while preserving the binary search tree property.
- Search: Looks for a specific value in the binary search tree.

# Tree traversal algorithms (pre-order, in-order, post-order)

Tree traversal algorithms are used to visit each node in a tree in a specific order. The three commonly used tree traversal algorithms are:

- Pre-order traversal: Visits the current node, then visits the left subtree, and finally visits the right subtree.
- In-order traversal: Visits the left subtree, then visits the current node, and finally visits the right subtree.
- Post-order traversal: Visits the left subtree, then visits the right subtree, and finally visits the current node.

# Balanced trees (AVL, Red Black)

Balanced trees are special types of trees that maintain a balanced structure, ensuring efficient search, insertion, and deletion operations. Two commonly used balanced tree structures are:

- AVL tree: A self-balancing binary search tree where the heights of the left and right subtrees differ by at most one.
- Red-Black tree: Another self-balancing binary search tree with additional color properties assigned to each node.

# Tree applications (expression evaluation, file systems)

Trees have various applications in computer science, including:

- Expression evaluation: Trees can represent mathematical expressions, where operators are internal nodes and operands are leaf nodes.
- File systems: Trees can model hierarchical file systems, with directories as internal nodes and files as leaf nodes.

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
