class Solution:
    def numSteps(self, s: str) -> int:
        ans = a = 0
        for i in s[:0:-1]:
            i = int(i) + a
            if i%2:
                ans += 2
                a = 1
            else:
                ans += 1
        return ans + a