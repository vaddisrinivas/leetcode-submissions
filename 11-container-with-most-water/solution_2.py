class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j, l = 0, len(height)-1, len(height)
        ma = 0
        while i<=j:
            b = j-i
            if height[i]>height[j]:
                h = height[j]
                j-=1
            elif height[i]<height[j]:
                h = height[i]
                i+=1
            else:
                h = height[j]
                i+=1
                j-=1
            ma = max(b*h,ma)
        return ma