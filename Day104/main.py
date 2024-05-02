class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        successor = None
        
        # Traverse the tree
        while A:
            if A.val > B:
                # If the current node's value is greater than B, update successor and move to the left subtree
                successor = A
                A = A.left
            else:
                # Move to the right subtree
                A = A.right
                
        return successor
