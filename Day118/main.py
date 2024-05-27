class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if nums[-1] == 0:
            return -1
        for i in range(len(nums)):
            if nums[i]>=n:
                return n
            n-=1
            if nums[i] >= n:
                return -1
        return -1