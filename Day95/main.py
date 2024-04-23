# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def postorderTraversal(self, A):
        ans = []
        s = [(A, False)]
        while s:
            node, visited = s.pop()
            if visited:
                ans.append(node.val)
            else:
                s.append((node, True))
                if node.right:
                    s.append((node.right, False))
                if node.left:
                    s.append((node.left, False))
        return ans