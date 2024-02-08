class Solution:
    def solve(self, A, B):
        ans=[]
        for i in range(1,len(A)):
            A[i] = max(A[i - 1], A[i])
        for i in range(len(B)):
            semians = -1
            l,r= 0,len(A)-1
            while l<=r:
                m=l+(r-l)//2
                if A[m]>=B[i]:
                    semians=m
                    r=m-1
                else:
                    l=m+1
            ans.append(semians)
        return ans
