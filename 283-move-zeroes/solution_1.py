# https://leetcode.com/problems/move-zeroes
# https://leetcode.com/problems/283-move-zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ct = 0
        l = len(nums)
        for i in range(l):
            if nums[i]==0:
                ct+=1
                continue
            else:
                nums[i-ct]=nums[i]
        for i in range(l-ct,l):
            nums[i]=0
            