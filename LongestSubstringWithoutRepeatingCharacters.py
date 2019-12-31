class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substrings = []
        max_len = 0
        for char in s:
            if char in substrings:
                substrings = substrings[substrings.index(char)+1:]
            substrings.append(char)
            current_len = len(substrings)
            if max_len < current_len:
                max_len = current_len
        return max_len
