# https://leetcode.com/problems/longest-increasing-subsequence
# https://leetcode.com/problems/300-longest-increasing-subsequence
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dup = [1]*len(nums)
        for i,j in enumerate(nums[1:],1):
            dup[i] += max([0] + [dup[k] for k,l in enumerate(dup[:i]) if nums[k]<j])
        return max(dup)
        