import bisect


class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums_bisect = []
        for num in nums:
            bisect.insort_right(nums_bisect, num)
        
        return nums_bisect[0]
