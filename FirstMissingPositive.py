class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        min_num = 1
        for i in nums:
            if i == min_num:
                min_num += 1
            if i > min_num:
                return min_num
        return min_num
