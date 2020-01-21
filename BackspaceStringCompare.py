class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S_modi = []
        for i in S:
            if i != '#':
                S_modi.append(i)
            else:
                if len(S_modi) > 0:
                    S_modi.pop()
        T_modi = []
        for i in T:
            if i != '#':
                T_modi.append(i)
            else:
                if len(T_modi) > 0:
                    T_modi.pop()
        
        if S_modi == T_modi:
            return True
        else:
            return False
        
