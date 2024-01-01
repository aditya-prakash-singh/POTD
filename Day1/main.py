class Solution:
    def canPair(self, nums, k):
        mods = [0 for _ in range(k)]
    	for item in nums: mods[item % k] += 1
        i, j = 1, k - 1
        while i < j:
            if mods[i] != mods[j]: return False
            i += 1
            j -= 1
        return mods[0] % 2 == 0 and (k % 2 == 1 or mods[k // 2] % 2 == 0)
