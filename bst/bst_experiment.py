class BSTNode(object):
    
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None 
    
    def is_leaf(self):
        return self.left is None and self.right is None
        
    def has_two_children(self):
        return self.left and self.right        
        
    
class BST(object):
    
    def __init__(self, r=None):
        self.root = r
        
    def add(self, val):
        if self.root is None:
            self.root = BSTNode(val)
        else:    
            BST.__add_to_tree__(self.root, val)
            
    @staticmethod    
    def __add_to_tree__(root_node, val):
        root_value = root_node.value
        if val == root_value:
            raise ValueError("Value {} is already found in tree".format(val))
        if val < root_value:
            if root_node.left:
                BST.__add_to_tree__(root_node.left, val)
            else:
                 root_node.left = BSTNode(val)
        else:
            if root_node.right:
                BST.__add_to_tree__(root_node.right, val) 
            else:
                 root_node.right = BSTNode(val)
    
    def search(self, val):
        return BST.__search_in_tree__(self.root, val)
            
    @staticmethod            
    def __search_in_tree__(root_node, val):
        if root_node is None:
            return False, None
        root_value = root_node.value
        if val == root_value:
            return True, root_node
        if val < root_value:
            return BST.__search_in_tree__(root_node.left, val)
        else:
            return BST.__search_in_tree__(root_node.right, val)
                
    def delete(self, val):                
        return BST.__search_and_delete__(None, self.root, val)
       
       
    @staticmethod        
    def __search_and_delete__(parent_node, node, val):
       if node is None:
           raise ValueError("Value {} is not found in the tree".format(val))
       node_value = node.value
       if node_value == val:
           BST.__delete__(parent_node, node)
           return
       if val < node_value:
           BST.__search_and_delete__(node, node.left, val)
       else:
           BST.__search_and_delete__(node, node.right, val)   
    
    @staticmethod           
    def __delete__(parent, node):
        if node.has_two_children():
            parent_of_smallest_node, smallest_node =  BST.__find_smallest_on_tree__(node, node.right)
            node.value = smallest_node.value
            BST.__delete_non_complete_node__(parent_of_smallest_node, smallest_node)   
            return
        else:
            BST.__delete_non_complete_node__(parent, node)
    
    @staticmethod
    def __find_smallest_on_tree__(parent, node):
        if node.left is None:
            return parent, node
        return BST.__find_smallest_on_tree__(node, node.left) 
           
    @staticmethod
    def __delete_non_complete_node__(parent, node):
        if node.is_leaf():
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
            return
        if node.left is None:
            parent.right = node.right
            return
        if node.right is None:
            parent.left = node.left
            return                                                            

    def pre_order_transverse(self):
        print("Pre-order tranversal")
        BST.__pre_order_transverse_tree__(self.root)
            
    @staticmethod    
    def __pre_order_transverse_tree__(root_node):
        if root_node is None:
            return
        print(root_node.value)
        if root_node.left:
            BST.__pre_order_transverse_tree__(root_node.left)            
        if root_node.right:
            BST.__pre_order_transverse_tree__(root_node.right)                
        
    def in_order_transverse(self):
        print("In-order tranversal")
        BST.__in_order_transverse_tree__(self.root)

    @staticmethod    
    def __in_order_transverse_tree__(root_node):
        if root_node is None:
            return
        if root_node.left:
            BST.__in_order_transverse_tree__(root_node.left)   
        print(root_node.value)         
        if root_node.right:
            BST.__in_order_transverse_tree__(root_node.right)
        
    def post_order_transverse(self):
        print("Post-order tranversal")
        BST.__post_order_transverse_tree__(self.root)

    @staticmethod    
    def __post_order_transverse_tree__(root_node):
        if root_node is None:
            return
        if root_node.left:
            BST.__post_order_transverse_tree__(root_node.left)        
        if root_node.right:
            BST.__post_order_transverse_tree__(root_node.right)
        print(root_node.value)                   
        

if __name__ == '__main__':
    node_values = [10, 5, 4, 7, 12, 33, 9, 17, 6, 27]
    bst = BST()
    for x in node_values:
        print("Adding value: {} to the binary search tree".format(x))
        try: 
            bst.add(x)
        except ValueError as e:
            print(str(e))
            continue               
    bst.pre_order_transverse()
    bst.in_order_transverse()
    
    bst.post_order_transverse()
    found, _ = bst.search(9)
    print("9 is {}found in the tree".format("" if found else "not "))
    found, _ = bst.search(13)
    print("13 is {}found in the tree".format("" if found else "not "))
    bst.delete(4)
    bst.post_order_transverse()
    bst.delete(12)
    bst.post_order_transverse()
    bst.delete(7)
    bst.post_order_transverse()
    bst.delete(20)    
        
    