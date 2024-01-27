class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        l=len(A)
        ans=0
        a=["a","e","i","o","u"]
        for i in range(l):
            if A[i].lower() in a:
                ans+=l-i
        return(ans%10003)
