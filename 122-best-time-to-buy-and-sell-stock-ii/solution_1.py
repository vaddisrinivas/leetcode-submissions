# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
# https://leetcode.com/problems/122-best-time-to-buy-and-sell-stock-ii
from pprint import pprint
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==1:
            return 0
        res = [0]*len(prices)
        res[1]=prices[1]-prices[0]
        for i in range(1,len(prices)):
            p = res[i-1]
            res[i] = max(p,p+prices[i]-prices[i-1])
        return res[-1]