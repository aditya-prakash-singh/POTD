class Solution:
    def sequence(self, n):
        ans=1
        idx=2
        first=2
        while idx<=n:
            temp=1
            for i in range(first,first+idx):
                temp=temp*i
            ans+=temp
            first=first+idx
            idx+=1
        return ans%(10**9+7)
