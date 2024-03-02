class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def spiralOrder(self, A):
        ans=[]
        while A:
            ans += A[0]
            A = A[1:]
            if A and A[0]:
                for i in A:
                    ans.append(i[-1])
                    i.pop(-1)
            if A:
                A=list(A)
                ans += A[-1][::-1]
                A.pop(-1)
            if A and A[0]:
                for i in A[::-1]:
                    ans.append(i[0])
                    i.pop(0)
        return ans
