class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        minv = prices[0]
        s = [0]
        for i in range(1, len(prices)):
            minv = min(minv, prices[i])
            s.append(prices[i]-minv)
        return max(s)
