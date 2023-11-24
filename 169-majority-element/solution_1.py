# https://leetcode.com/problems/majority-element
# https://leetcode.com/problems/169-majority-element
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s = Counter(nums)
        l = len(nums)
        for i in s:
            if s[i]>l/2:
                return i
        