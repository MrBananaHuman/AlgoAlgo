class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        result = []
        splited_text = text.split(' ')
        for i in range(0, len(splited_text) - 2):
            pre = splited_text[i]
            post = splited_text[i+1]
            if pre == first and post == second:
                result.append(splited_text[i+2])
        return result
