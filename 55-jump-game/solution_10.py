# https://leetcode.com/problems/jump-game
# https://leetcode.com/problems/55-jump-game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        p = len(nums)-1
        for i in range(p,-1,-1):
            if i+nums[i]>=p:
                p = i
        return p==0

