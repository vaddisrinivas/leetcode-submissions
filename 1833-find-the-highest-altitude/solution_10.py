# https://leetcode.com/problems/find-the-highest-altitude
# https://leetcode.com/problems/1833-find-the-highest-altitude
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        m = 0
        s = 0
        for i in gain:
            s += i
            m = max(s,m)
        return m
        