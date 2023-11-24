# https://leetcode.com/problems/longest-increasing-subsequence
# https://leetcode.com/problems/300-longest-increasing-subsequence
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dup = [1]*len(nums)
        for i,j in enumerate(nums[1:],1):
            prev = [dup[k] for k,l in enumerate(dup[:i]) if nums[k]<j]
            dup[i] += max(prev) if prev else 0
        return max(dup)
        