class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextPermutation(self, A):
        l,a=len(A),len(A)-2
        while(a>= 0 and A[a]>=A[a+1]):
            a-=1
        if a == -1:
            A.reverse()
            return A
        b=l-1
        while(not A[a]<A[b]):
            b-=1
        A[a],A[b]=A[b],A[a]
        A[a+1:]=A[a+1:][::-1]
        return A