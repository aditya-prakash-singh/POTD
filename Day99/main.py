# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
def dd( node, target, current_sum):
    if node is None:
        return False
    current_sum += node.val
    if node.left is None and node.right is None:
        return current_sum == target
    return dd(node.left, target, current_sum) or dd(node.right, target, current_sum)
class Solution:
	# @param A : root node of tree
	# @param B : integer
	# @return an integer
    def hasPathSum(self, A, B):
        return 1 if dd(A,B,0) else 0
