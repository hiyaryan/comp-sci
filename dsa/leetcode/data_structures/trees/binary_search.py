# Binary search trees are great for searching.

# Best case scenario
# lookup: O(log n)
# insert: O(log n)
# delete: O(log n)
# This occurs when a linked list is balanced. To balanced binary search tree can be implemented using e.g. AVL or Red Black algorithms

# Worst case scenario
# lookup: O(n)
# insert: O(n)
# delete: O(n)
# This occurs when the tree becomes unbalanced and essentially turns into a linked list.
import json


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """
        Inserts a node into the binary search tree.
        """
        # insert the first node into the tree
        if self.root == None:
            self.root = Node(value)

        else:
            parent_node = None
            next_node = self.root

            # keep looping until next_node (a child_node of parent_node) is None
            while next_node:
                # parent_node will always be one level less than next_node
                parent_node = next_node

                # if less set next_node equal to left node of parent_node
                if value < next_node.value:
                    next_node = None if not parent_node.left else parent_node.left

                # if greater next_node equal to right node of parent_node
                else:
                    next_node = None if not parent_node.left else parent_node.right

            # set left child node of parent_node if value is less than parent value
            if value < parent_node.value:
                parent_node.left = Node(value)

            # set right child node of parent_node if value is greater than parent value
            else:
                parent_node.right = Node(value)

    def lookup(self, value):
        next_node = self.root

        while next_node:
            # get the left child if value is less than parent value
            if value < next_node.value:
                next_node = next_node.left

            # get the right child is value is greater than parent value
            elif value > next_node.value:
                next_node = next_node.right

            # otherwise return the parent which is the lookup value
            else:
                return next_node

        # no lookup value found
        return None

    def remove(self, value):
        pass


def traverse(node):
    parent_value = getattr(node, "value", None)
    tree = {"value": parent_value}

    left_child = getattr(node, "left", None)
    tree["left"] = None if not left_child else traverse(left_child)

    right_child = getattr(node, "right", None)
    tree["right"] = None if not right_child else traverse(right_child)

    return tree


def main():
    #        9
    #    4       20
    # 1    6  15    170

    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)

    json_tree = json.dumps(traverse(tree.root))
    print(json_tree)

    # lookup 20, 6, 3, and 25
    print(json.dumps(traverse(tree.lookup(20))))
    print(json.dumps(traverse(tree.lookup(6))))
    print(json.dumps(traverse(tree.lookup(3))))
    print(json.dumps(traverse(tree.lookup(25))))


if __name__ == "__main__":
    main()
