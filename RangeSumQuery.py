class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            return None
        self.dps = [0] * len(nums)
        self.dps[0] = nums[0]
        for i in range(1, len(nums)):
            self.dps[i] = self.dps[i-1] + nums[i]
        
    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.dps[j]
        else:
            return self.dps[j] - self.dps[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
