# https://leetcode.com/problems/house-robber
# https://leetcode.com/problems/198-house-robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 8,7,8,9,7,8
        # 8,7,16,17,23,25
        # 2,7,9,3,1
        # 2,7,11,10,12
        # 7,2,3,9,1
        # 7,2,10,16,11
        if len(nums)<=2:
            return max(nums)
        nums[2] += nums[0]
        if len(nums)==3:
            return max(nums)
        for ind,i in enumerate(nums[3:],3):
            nums[ind] += max(nums[ind-2],nums[ind-3])
        return max(nums[-1],nums[-2])