# https://leetcode.com/problems/find-pivot-index
# https://leetcode.com/problems/724-find-pivot-index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        temp = 0
        for i,j in enumerate(nums):
            if temp==s-temp-j:
                return i
            temp+=j
        return -1