# https://leetcode.com/problems/single-number
# https://leetcode.com/problems/136-single-number
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = {}
        for i in nums:
            if i in s:
                s[i] += 1
            else:
                s[i] = 1
        for i in s:
            if s[i]==1:
                return i