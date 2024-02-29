class Solution:
    # @param A : list of integers
    # @return an integer
    def divisibleBy60(self, A):
        if A==[0]:
            return(1)
        if 0 not in A:
            return(0)
        if sum(A)%3!=0:
            return(0)
        if any(i%2==0 for i in A if i!=0):
            return(1)
        return(0)
