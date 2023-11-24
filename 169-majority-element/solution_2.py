# https://leetcode.com/problems/majority-element
# https://leetcode.com/problems/169-majority-element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        i,j,l = 0,0,len(nums)
        mc,c = 0,0
        while i<l and j<l:
            if nums[i]==nums[j]:
                c += 1
                j += 1
            else:
                mc = max(c,mc)
                if mc>l/2:
                    break
                c = 0
                i = j
        return nums[j-1]