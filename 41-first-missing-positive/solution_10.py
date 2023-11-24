# https://leetcode.com/problems/first-missing-positive
# https://leetcode.com/problems/41-first-missing-positive
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = set(nums)
        i = 1
        while True:
            if i not in nums:
                break
            i += 1
        return i
        