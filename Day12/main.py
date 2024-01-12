class Solution:
    def modifyQueue(self, q, k):
        q=q[:k][::-1]+q[k:]
        return(q)
