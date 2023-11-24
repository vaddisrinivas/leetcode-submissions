# https://leetcode.com/problems/remove-duplicates-from-sorted-array
# https://leetcode.com/problems/26-remove-duplicates-from-sorted-array
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        i,j,k = 0, 1,1
        l = len(nums)
        if l==2:
            return 2 if nums[0]!=nums[1] else 1
        while i<l-1:
                
            if nums[i]==nums[j]:
                j+=1
            else:
                nums[k]=nums[j]
                i = j
                j+=1
                k+=1
            if j==l and k!=l:
                nums[k]=nums[j-1]
                break
        return k