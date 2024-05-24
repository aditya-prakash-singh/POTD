from typing import List


class Solution:
    
    mod = 10**9 + 7

    def solve(self, i, sum, arr):
        if i == 0:
            if sum == 0:
                return 1
            return 0

        ans = self.solve(i - 1, sum, arr)

        if sum >= arr[i - 1]:
            ans = (ans + self.solve(i - 1, sum - arr[i - 1], arr)) % self.mod

        return ans
        
    def countPartitions(self, n, d, arr):
        # Code here
        totalSum = sum(arr)

        if totalSum < d or (totalSum - d) % 2 != 0:
            return 0

        target = (totalSum - d) // 2

        return self.solve(n, target, arr)