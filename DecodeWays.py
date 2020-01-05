class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dps = [0]*(n+1)
        dps[0] = 1
        for i in range(1, n+1):
            cnt = 0
            if i-1 >= 0 and int(s[i-1]) > 0:
                cnt += dps[i-1]
            if i-2 >= 0 and int(s[i-2:i]) >= 10 and int(s[i-2:i]) <= 26:
                cnt += dps[i-2]
            dps[i] = cnt
        return dps[n]
