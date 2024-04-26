# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))
class Solution:
	# @param A : root node of tree
	# @return an integer
    def isBalanced(self, A):
        if A is None:
            return 1
        if abs(height(A.left) - height(A.right)) > 1:
            return 0
        return self.isBalanced(A.left) and self.isBalanced(A.right)