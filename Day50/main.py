class Solution:
    def maxSum(self, n): 
        # code here 
        if n<12:
            return n
        else:
            return self.maxSum(n//2)+self.maxSum(n//3)+self.maxSum(n//4)
