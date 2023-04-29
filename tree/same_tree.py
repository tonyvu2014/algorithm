# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Tranverse 2 trees simultaniously, at every step, compare nodes from the 2 trees  
# If there is difference at one step, return False
# Return True at the end
def is_same_tree(p, q):
    if p is None:
       return q is None

    if q is None:
        return p is None
    
    if p.val != q.val:
        return False
    else:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

if __name__ == '__main__':
    left = TreeNode(1, None, None)
    right = TreeNode(2, None, None)
    p = TreeNode(1, left, right)

    l = TreeNode(1, None, None)
    r = TreeNode(2, None, None)
    q = TreeNode(1, l, r)

    print(is_same_tree(p, q))

