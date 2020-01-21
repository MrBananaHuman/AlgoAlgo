class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        result = []
        par_num = 0
        for i in S:
            if i == '(':
                par_num += 1
            if par_num > 1:
                result.append(i)
            if i == ')':
                par_num -= 1
        return ''.join(result)
