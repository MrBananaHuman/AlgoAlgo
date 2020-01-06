class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dps = [0] * len(nums)
        dps[0] = nums[0]
        for i in range(1, len(nums)):
            dps[i] = max(nums[i], nums[i] + dps[i-1])
        return max(dps)
        
