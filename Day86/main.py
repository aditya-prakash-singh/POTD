class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        l=len(A)
        a=[[0]*l for _ in range(l)]
        for i in range(l):
            for j in range(l):
                a[i][j]=A[j][i]
        for i in range(l):
            A[i]=a[i][::-1]
        return(A)