mod=10**9+7
class Solution:
    def padovanSequence(self, n):
        a,b,c=1,1,1
        for i in range(3,n+1):
            a,b,c=b,c,(a+b)%mod
        return c