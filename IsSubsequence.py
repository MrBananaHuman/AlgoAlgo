class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        current_s_num = 0
        if not s:
            return True
        if not t:
            return False
        for char in t:
            current_s_char = s[current_s_num]
            if char == current_s_char:
                current_s_num += 1
            if current_s_num == len(s):
                return True
        if current_s_num == len(s):
            return True
        else:
            return False
