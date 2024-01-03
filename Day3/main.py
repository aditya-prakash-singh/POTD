from collections import defaultdict

class Solution:
    def smallestSubstring(self, S):
        a = defaultdict(int)
        
        k = 0
        ans = float('inf')
        for i, j in enumerate(S):
            a[j] += 1
            while len(a) >= 3:
                ans = min(ans, i - k + 1)
                a[S[k]] -= 1
                if a[S[k]] == 0:
                    a.pop(S[k])
                k += 1

        return -1 if ans == float('inf') else ans
