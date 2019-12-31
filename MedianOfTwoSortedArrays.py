class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        median = 0
        if len(nums1) % 2 == 1:
            median = nums1[int(len(nums1)/2)]
        else:
            median = (nums1[int(len(nums1)/2)] + nums1[int(len(nums1)/2)-1])/2
        return median
