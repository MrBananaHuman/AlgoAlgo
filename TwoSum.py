class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for i, num in enumerate(nums):
            current_num = nums[i]
            target_num = target - current_num
            if i > len(nums):
                break
            for j, inner_num in enumerate(nums[i+1:len(nums)]):
                if inner_num == target_num:
                    result.append(i)
                    result.append(i+1+j)
                    return result
