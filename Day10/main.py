class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        ans,ans1=0,0
        for i in A:
            if i>C:
                ans+=1
        for j in B:
            if j<C:
                ans1+=1
        return(max(ans,ans1))
        
                
