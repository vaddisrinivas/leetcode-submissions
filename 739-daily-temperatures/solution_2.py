# https://leetcode.com/problems/daily-temperatures
# https://leetcode.com/problems/739-daily-temperatures
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        l = len(temperatures)
        s = []
        res = [0]*l
        for ind, i in enumerate(temperatures):
            while s and s[-1][0]<i:
                p = s.pop()
                res[p[1]]=ind-p[1]
            s.append((i,ind))
       
        return res