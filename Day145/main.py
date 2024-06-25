# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, r: Optional[TreeNode]) -> Optional[TreeNode]:
        def f(n, q):
            if n:
                n.val += f(n.right, q)
                return f(n.left, n.val)
            return q
        f(r, 0)
        return r