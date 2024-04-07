class Solution:
    # @param A : tuple of integers
    # @return an integer
    def findMin(self, A):
        l=len(A)
        st,end=0,l-1
        while(st<=end):
            c=(st+end)//2
            a=(c+1)%l
            if A[c]>A[a]:
                return(A[a])
            if A[c]>=A[st]:
                st=c+1
            else:
                end=c-1
        return(1)