class Solution:
    # @param A : list of integers
    # @return an integer
    def maximumGap(self, A):
        l=len(A)
        a,b=[0]*l,[0]*l
        a[0]=A[0]
        for i in range(1,l):
            a[i]=min(a[i-1], A[i])
        
        b[l - 1] = A[l - 1]
        for i in range(l - 2, -1, -1):
            b[i] = max(b[i + 1], A[i])
        
        ans=0
        i,j=0,0
        while i<l and j<l:
            if a[i]<=b[j]:
                ans=max(ans,j-i)
                j+=1
            else:
                i+=1
        return(ans)