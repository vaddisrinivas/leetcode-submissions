# https://leetcode.com/problems/min-cost-climbing-stairs
# https://leetcode.com/problems/747-min-cost-climbing-stairs
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)-3
        while l>=0:
            m = min(cost[l+1],cost[l+2])
            cost[l] += m
            l -= 1
        return min(cost[0],cost[1])

        