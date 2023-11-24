# https://leetcode.com/problems/house-robber
# https://leetcode.com/problems/198-house-robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        nums[2] += nums[0]
        if len(nums)==3:
            return max(nums)
        for ind,i in enumerate(nums[3:],3):
            nums[ind] += max(nums[ind-2],nums[ind-3])
        return max(nums[-1],nums[-2])