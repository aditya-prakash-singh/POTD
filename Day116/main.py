class Solution:
    #Your task is to complete this function
    #Function should return an integer
    #a - list/array containing height of stack's respectively
    def max_Books(self, n, k, arr):
        curr,ans=0,0
        for item in arr:
            if item<=k:
                curr+=item
            else:
                ans=max(ans,curr)
                curr=0
        return max(ans,curr)