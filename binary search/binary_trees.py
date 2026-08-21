# binary tree
class TreeNode:
    def __init__(self,val,right=None,left=None): # A constructor 
        self.val = val
        self.right = right
        self.left = left
    def __str__(self): # A method
        return str(self.val) # to confirm, if you want to print any reference of a  tree node, we print the value of the node.

# IF WE WANT TO CREATE THE TREE:
#           1
#       2         3
#   4      5   10

#           = 

A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left  = D
B.right = E
C.left = F
# Test
print(A.left, "** \n ")
print('---------------------', 'PRE-ORDER ')
# Recursive Pre-order Traversal(DFS) Time comp: O(n), Space comp = O(n)
def pre_order(node):
    # Base-case
    if not node:
        return 
    # steps of pre-order = node -> left -> right
    print(node)
    pre_order(node.left)
    pre_order(node.right)
    
# Now we can test on our tree, by putting the root in the argument of the function:
pre_order(A)
print('---------------------', 'IN-ORDER')
# Recursive in-order Traversal(DFS) Time comp: O(n), Space comp = O(n)
def in_order(node):
    # Base-case
    if not node:
        return 
    # steps of pre-order = node -> left -> right
    in_order(node.left)
    print(node)
    in_order(node.right)
in_order(A)
print('---------------------', 'POST-ODER')
# Recursive post-order Traversal(DFS) Time comp: O(n), Space comp = O(n)
def post_order(node):
    # Base-case
    if not node:
        return 
    # steps of pre-order = node -> left -> right
    post_order(node.left)
    post_order(node.right)
    print(node)
post_order(A)
print('---------------------', 'ITERATIVE PRE-ORDER')
# Iterative Traversal(DFS) - leads to Pre-order Traversal(DFS) Time comp: O(n), Space comp = O(n)
def pre_order_iterative(node):
    stck = [node] # create a stack 
    while stck: # while there are nodes in the stack 
        node = stck.pop() # remove them(remove the node at the top of the stack)
        print(node) # then print 
        if node.right:
            stck.append(node.right) # start with right, so we can we have [right,left] and pop to remove left 
        if node.left:
            stck.append(node.left) # this force us to move left in the tree 
pre_order_iterative(A)
print('---------------------', 'BFS(LEVEL-ORDER TRAVERSAL)')
# Level Order Traversal(BFS) Time comp : O(n), Space comp = O(n)
from collections import deque 
def level_order_traversal(node):
    q = deque() # creates like a queue but you can remove and delete element from the from the left or right.
    q.append(node)
    while q:
        node = q.popleft()
        print(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
level_order_traversal(A)
print('---------------------', 'CHECKING IF VALUE EXISTS(DFS)')
# Checking if value exists(DFS) Time comp: O(n), Space comp = 0(n)
def search(node, target):
    if not node: # if we dont find the target , we return false
        return False
    if node.val == target: #if the actual value is the equal to the node
        return True  
    
    return search(node.left, target) or search(node.right, target) # check the right and the left,
                                                                # keep on doing this till you find the target
print(search(A, 10), ' : checks if 10 is in the tree')

