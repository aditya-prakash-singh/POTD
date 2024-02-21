import math
class Solution:
    # @param A: integer
    # @return a list of integers
    def allFactors(self, A):
        ans=[]
        for i in range(1,int(math.sqrt(A)+1)):
            if A%i==0:
                ans.append(i)
                if i!=A//i:
                    ans.append(A//i)
        ans.sort()
        return ans
