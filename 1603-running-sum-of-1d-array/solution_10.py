# https://leetcode.com/problems/running-sum-of-1d-array
# https://leetcode.com/problems/1603-running-sum-of-1d-array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prev = 0
        for i,j in enumerate(nums):
            prev += j
            nums[i] = prev
        return nums