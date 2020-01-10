class Solution:
    def largestNumber(self, nums):

        class Predicate(str):
            def __lt__(self, other):
                return self + other < other + self

        strs = ''.join(sorted(map(str, nums), key=Predicate, reverse=True))
        return '0' if strs[0] == '0' else strs
