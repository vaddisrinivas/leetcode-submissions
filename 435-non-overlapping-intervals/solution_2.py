# https://leetcode.com/problems/non-overlapping-intervals
# https://leetcode.com/problems/435-non-overlapping-intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]])-> int:
        # l = len(intervals)
        intervals.sort(reverse=True)
        mx = intervals[0]
        c = 0
        for i in intervals[1:]:
            if i[1] <= mx[0]:
                mx = i
            else:
                c+= 1
        return c

        # dp = {}
        # dp[l-1] = 1
        # def dfs(ind):
        #     if ind >= l:
        #         return 0
        #     if ind in dp:
        #         return dp[ind]
        #     c = 0
        #     for i in range(ind + 1, l):
        #         if intervals[i][0] >= intervals[ind][1] and dp[i] > c:
        #             c = dp[i]   
        #     dp[ind] = c + 1
        #     return dp[ind]
        # mn = 0
        # for i in range(l-1,-1,-1):
        #     curr = dfs(i)
        #     if curr > mn:
        #         mn = curr

        # return l - mn 
         