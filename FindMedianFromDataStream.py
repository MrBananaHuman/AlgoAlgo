class MedianFinder:

    def __init__(self):
        self.nums = []
        
    def addNum(self, num: int) -> None:
        self.nums.append(num)
        

    def findMedian(self) -> float:
        total_num = 0
        self.nums.sort()
        if len(self.nums) % 2 == 1:
            return self.nums[int(len(self.nums)/2)]    
        else:
            median_num = int(len(self.nums) / 2)
            return (self.nums[median_num] + self.nums[median_num - 1])/2
        
