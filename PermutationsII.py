from itertools import permutations 

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result_set = set()
        result = []
        perm = permutations(nums)
        for i in list(perm):
            result_set.add(i)
        for k in result_set:
            result.append(list(k))
        return result
