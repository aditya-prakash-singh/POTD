class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        a,l={},len(A) 
        for i in range(l): 
            if A[i] not in a: 
                a[A[i]]=1 
            else: 
                ans=A[i] 
                break 
        sumi=(l*(l+1))//2 
        return(ans,abs(sumi-sum(A)+ans))