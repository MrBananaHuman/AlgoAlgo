class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        modi_list = []
        for word in s.split(' '):
            word = word.strip()
            if len(word) > 0:
                modi_list.append(word)
        modi_list.reverse()
        return ' '.join(modi_list)
        
