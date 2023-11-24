# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons
# https://leetcode.com/problems/452-minimum-number-of-arrows-to-burst-balloons
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points)==1:
            return 1
        c = 0
        points.sort(key=lambda x: x[1])
        # print(points)
        i, l = 1, len(points)
        s,m = points[0]
        while i<l:
            # print(m,c,points[i][1])
            if m<points[i][0]:
                m = points[i][1]
                c += 1
            i += 1
        return c+1
