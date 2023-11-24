# https://leetcode.com/problems/missing-number
# https://leetcode.com/problems/268-missing-number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)+1
        expected =  l*(l-1)//2
        return expected-sum(nums)
