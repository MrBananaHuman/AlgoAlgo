class Solution(object):
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        maxn = 0
        f = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1] == '1':
                    f[i][j] = 1 + min(f[i-1][j], f[i][j-1], f[i-1][j-1])
                    maxn = max(maxn, f[i][j])
        return maxn**2
