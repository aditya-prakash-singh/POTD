# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

def check(left, right):
    if not left and not right:
        return 1
    if not left or not right:
        return 0
    if left.val != right.val:
        return 0
    return check(left.left, right.right) and check(left.right, right.left)
	
class Solution:
	# @param A : root node of tree
	# @return an integer
	def isSymmetric(self, A):
        if not A:
            return 1
        return check(A.left, A.right)