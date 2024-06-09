class Solution:
    def findExtra(self,n,a,b):
        xor = 0
        for i in range(len(b)):
            xor = xor ^ a[i] ^ b[i]
        xor = xor^a[-1]
        return a.index(xor)