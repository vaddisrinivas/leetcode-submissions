# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
# https://leetcode.com/problems/80-remove-duplicates-from-sorted-array-ii
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        i, j, k, l, c = 0, 0, 0, len(nums),-1
        while i<l and j<l:
            if nums[i]==nums[j]:
                c += 1
                if c<2:
                    nums[k] = nums[j]
                    k += 1
                j+=1
            else:
                c = -1
                i = j
        return k