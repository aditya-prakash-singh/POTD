class Solution:
    def kthCommonAncestor(self, root, k, x, y):
        l=[]
        while True:
            l.append(root.data)
            if root.data< x and root.data <y:
                root=root.right
            elif root.data >x and root.data>y:
                root=root.left
            else:
                break
        if len(l)<k:
            return(-1)
        else:
            return(l[-k])