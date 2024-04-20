# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def preorderTraversal(self, A):
        s=[A]
        ans=[]
        while(s):
            a=s[-1]
            ans.append(a.val)
            s.pop()
            if(a.right):
                s.append(a.right)
            if(a.left):
                s.append(a.left)
        return ans