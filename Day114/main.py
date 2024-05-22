class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def f(s):
            if s:
                ans = []
                for j in range(len(s)):
                    if s[:j+1] == s[:j+1][::-1]:
                        for p in f(s[j+1:]):
                            ans.append([s[:j+1]]+p)
                return ans
            return [[]]
        return f(s)