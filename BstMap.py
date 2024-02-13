from dataclasses import dataclass
from typing import Any

# The BstMap class is a binary search tree based implementation of
# a map (or dictionary). It works for any type of values and for
# all types keys that are comparable ==> we can compare keys using
# the operators < and >.


# The Node class is responsible for most of the work.
# Each call to the BstMap class is just delegated to the
# root node which starts a recursive sequence of calls to
# handle the request. Notice: All Node methods are recursive.
@dataclass
class Node:
    key: Any = None         # the key
    value: Any = None       # the value
    left: Any = None        # left child (a Node)
    right: Any = None       # right child (a Node)

    # Inserts a key-value pair into the tree
    def put(self, key, value):
        # Add left node if given key is less than current node
        if self.key > key:
            if self.left is None:
                self.left = Node(key, value)
            else:
                self.left.put(key, value)

        # Add right node if given key is more than current node
        elif self.key < key:
            if self.right is None:
                self.right = Node(key, value)
            else:
                self.right.put(key, value)

        # If key is current key
        else:
            self.value = value

    # Returns a string representation of the tree
    def to_string(self):
        # Get string representation of left key
        if self.left:
            left_str = self.left.to_string()
        else:
            left_str = ""

        # Get string representation of root
        root_str = f"({self.key}, {self.value}) "

        # Get string representation of right key
        if self.right:
            right_str = self.right.to_string()
        else:
            right_str = ""

        # Return all strings added to each other, left to right
        return left_str + root_str + right_str

    # Returns the total number of nodes in the tree
    def count(self):
        # Initialize count variable
        count = 1

        # Check if left and right nodes exists, if so,
        # recursivelly call count() on them and add to the count variable
        if self.left:
            count += self.left.count()
        if self.right:
            count += self.right.count()

        return count

    # Gets the value for a given key
    def get(self, key):
        # If current key matches desired key
        if self.key == key:
            return self.value

        # If desired key is less than left key
        # and left child exists
        elif key < self.key and self.left:
            return self.left.get(key)

        # If desired key is more than left key
        # and left child exists
        elif key > self.key and self.right:
            return self.right.get(key)

    # Returns the maximum depth of the tree, that is;
    # the amount of nodes on the "edge" of the tree
    def max_depth(self):
        # Calculate the maximum depth of the left subtree
        left_depth = self.left.max_depth() if self.left else 0

        # Calculate the maximum depth of the right subtree
        right_depth = self.right.max_depth() if self.right else 0

        # Return the maximum depth of either subtree
        # plus 1 for the current node
        return max(left_depth, right_depth) + 1

    # Counts the number of internal nodes (nodes with at least one child)
    def count_internal_nodes(self):

        # Initialize count variable
        count = 0

        # If the current Node has any childitem increment count
        if self.left or self.right:
            count += 1

        # If Node has a childitem on the left recursively call the method
        # and add add the additional count to the count variable
        if self.left:
            count += self.left.count_internal_nodes()

        # If Node has a childitem on the right recursively call the method
        # and add add the additional count to the count variable
        if self.right:
            count += self.right.count_internal_nodes()

        return count

    # Returns a list of key-value pairs in in-order traversal
    def as_list(self, lst):
        # Recursivelly call as_list on
        # all left nodes
        if self.left:
            self.left.as_list(lst)

        # Append the key and value to the list
        lst.append((self.key, self.value))

        # Recursivelly call as_list on
        # all right nodes
        if self.right:
            self.right.as_list(lst)

        return lst


# The BstMap class is rather simple. It basically just takes care
# of the case when the map is empty. All other cases are delegated
# to the root node ==> the Node class.
@dataclass
class BstMap:
    root: Node = None

    # Adds a key-value pair to the map
    def put(self, key, value):
        if self.root is None:    # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        if self.root is None:     # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += str(self.root.to_string())
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns an internal node count. That is, the number of nodes
    # that has aleast one child (i.e. not leafs)
    def count_internal_nodes(self):
        if self.root is None:
            return 0
        else:
            return self.root.count_internal_nodes()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)
