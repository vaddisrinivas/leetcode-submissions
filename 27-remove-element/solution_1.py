# https://leetcode.com/problems/remove-element
# https://leetcode.com/problems/27-remove-element
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i,j = 0,len(nums)-1
        l = len(nums)
        while i<=j:
            if nums[j]==val:
                j-=1
                continue
            if nums[i]==val:
                nums[i],nums[j]= nums[j],nums[i]
                j -= 1
            i += 1
        return  j+1 if i>j else 0

            