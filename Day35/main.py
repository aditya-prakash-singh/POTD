class Solution:
    def solve(self, A):
        a=0
        b=len(A)-1
        ans=[]
        while(a<=b):
            if A[a]>A[b]:
                ans.append(A[a])
                a+=1
            else:
                ans.append(A[b])
                return(ans+A[a:-1][::-1])
        return(ans)

