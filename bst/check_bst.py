#####
# Check if a given tree is a binary search tree
# min-max algorithm
######

import sys

class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right =  None

    def set_left(self, node):
        self.left = node

    def set_right(self, node):
        self.right = node 


def isBST(node):
    return isBSTMinMax(node, -sys.maxsize-1, sys.maxsize)


def isBSTMinMax(node, minValue, maxValue):
    if node is None:
        return True

    if node.data > maxValue or node.data < minValue:
        return False

    return isBSTMinMax(node.left, minValue, node.data) and \
        isBSTMinMax(node.right, node.data, maxValue)   


if __name__=='__main__': 
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    print(isBST(root))