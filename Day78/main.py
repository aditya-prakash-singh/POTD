class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        return(bin(A)[2::].count('1'))