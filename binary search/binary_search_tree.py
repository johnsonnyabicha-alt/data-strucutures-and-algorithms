# Binary Search Trees (BSTs)
class BinarySearchTreeNode:
    def __init__(self,val,right=None,left=None): # A constructor 
        self.val = val
        self.right = right
        self.left = left
    def __str__(self): # A method
        return str(self.val) # to confirm, if you want to print any reference of a  tree node, we print the value of the node.

# CREATING A BINARY SEARCH TREE:
#               5
#           1      8
#       -1    3  7   9
A =  BinarySearchTreeNode(5)
B =  BinarySearchTreeNode(1)  
C =  BinarySearchTreeNode(8)
D =  BinarySearchTreeNode(-1) 
E =  BinarySearchTreeNode(3)
F =  BinarySearchTreeNode(7)
G =  BinarySearchTreeNode(9)

A.left, A.right = B, C
B.left, B.right = D, E
C.left, C.right = F, G 
print(A, " ** ")
print('---------------------', 'IN-ORDER, ORDERING THE NODES(WORKS ON BINARY SEARCH TREE ONLY)')
def in_order(node):
    # base case 
    if not node:
        return
    in_order(node.left)
    print(node)
    in_order(node.right)
in_order(A)
print('---------------------', 'SEARCHING')
def search_bst(node, target):
    if not node: # if we dont find the target, which is the particular node we are looking for, return false
        return False
    if node.val == target:
        return True 
    if target < node.val: # if the target is on the left, basically lower than the current node, keep on search on the left.
        return search_bst(node.left, target)
    else: # if target is on the right, keep on looking on the right 
        return search_bst(node.right, target)
print(search_bst(A, 9))
