# https://leetcode.com/problems/squares-of-a-sorted-array
# https://leetcode.com/problems/1019-squares-of-a-sorted-array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0 
        j = len(nums)-1
        sq = [0]*len(nums)
        sqi=j
        while i<=j:
            if abs(nums[i])<abs(nums[j]):
                sq[sqi]=nums[j]**2
                j-=1
            else:
                sq[sqi]=nums[i]**2
                i+=1
            sqi-=1
        return sq