# https://leetcode.com/problems/container-with-most-water
# https://leetcode.com/problems/11-container-with-most-water
from pprint import pprint
class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        def area(l,b):
            return l*b

        l = len(height)
        if l==2:
            return area(1,min(height[0],height[1]))
        m1, m2 = 0, l-1
        max_area = 0
        area_temp = 0
        while m1<=m2 :
            # pprint(locals())
            if height[m1]>height[m2]:
                area_temp = area(m2-m1, height[m2])
                m2 -= 1
            else:
                area_temp = area(m2-m1, height[m1])
                m1 += 1
            if area_temp > max_area:
                max_area = area_temp
            # pprint("*"*10)
            # pprint(locals())
            # pprint("-"*10)
        return max_area
        
