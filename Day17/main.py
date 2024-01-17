import itertools
class Solution:
    def uniquePerms(self, arr, n):
        # code here 
        permutations = itertools.permutations(arr)
        ans = set()
        for perm in permutations:
            ans.add(perm)
        ans = list(ans)
        ans.sort()
        return ans
