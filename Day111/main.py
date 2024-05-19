from typing import List

class Solution:
    def findClosest(self,n,k,arr):
        ans=abs(arr[-1]-k)
        answer=arr[-1]
        for i in reversed(arr):
            if abs(k-i)<ans:
                answer=i
                ans=abs(k-i)
        return(answer)