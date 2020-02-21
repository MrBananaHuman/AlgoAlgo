class Solution:
    def mergeSort(self, myList) -> None:
        if len(myList) > 1:
            mid = len(myList) // 2
            left = myList[:mid]
            right = myList[mid:]

            self.mergeSort(left)
            self.mergeSort(right)

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                  myList[k] = left[i]
                  i += 1
                else:
                    myList[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                myList[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                myList[k]=right[j]
                j += 1
                k += 1
    
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.mergeSort(nums)
        
        
