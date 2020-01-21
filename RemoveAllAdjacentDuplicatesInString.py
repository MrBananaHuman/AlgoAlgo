class Solution:
    def removeDuplicates(self, S: str) -> str:
        result = ['']
        for i in S:
            if result[-1] == i and len(result) > 0:
                result.pop()
            else:
                result.append(i)
        return ''.join(result)
        
