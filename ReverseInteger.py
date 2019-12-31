class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = -x
            s = str(x)
            r_s = -int(s[::-1])
            if r_s >= 2**31-1 or r_s <= -2**31:
                return 0
            return r_s
        else:
            s = str(x)
            r_s = int(s[::-1])
            if r_s >= 2**31-1 or r_s <= -2**31:
                return 0
            return r_s
        
