class Solution:
    def countNumberswith4(self, n : int) -> int:
        # code here
        ans = 0
        for i in range(1,n+1):
            if "4" in str(i):
                ans += 1
        return ans