class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = ['']
        chars = dict()
        chars['2'] = ['a', 'b', 'c']
        chars['3'] = ['d', 'e', 'f']
        chars['4'] = ['g', 'h', 'i']
        chars['5'] = ['j', 'k', 'l']
        chars['6'] = ['m', 'n', 'o']
        chars['7'] = ['p', 'q', 'r', 's']
        chars['8'] = ['t', 'u', 'v']
        chars['9'] = ['w', 'x', 'y', 'z']
        
        chars_list = []
        
        for i in digits:
            current_chars = chars[i]
            temp = []
            for char in current_chars:
                for str in result:
                    temp.append(str+char)
            result = temp
        return result
        
        
