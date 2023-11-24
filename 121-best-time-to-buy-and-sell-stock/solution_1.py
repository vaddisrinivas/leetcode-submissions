# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# https://leetcode.com/problems/121-best-time-to-buy-and-sell-stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit, profit, curr_min = 0, 0, prices[0]
        i = 1
        while i<len(prices):
            j = prices[i]
            curr_profit = j - curr_min
            if curr_profit>profit:
                profit = curr_profit
            if prices[i]<curr_min:
                curr_min = prices[i]
            i += 1
        return profit
            


