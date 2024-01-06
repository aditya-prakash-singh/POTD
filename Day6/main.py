class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        l=len(A)
        return((pow(2,l)-1)%1000000007)
