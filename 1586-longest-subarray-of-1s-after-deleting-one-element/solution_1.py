# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element
# https://leetcode.com/problems/1586-longest-subarray-of-1s-after-deleting-one-element
class Solution:
   def longestSubarray(self, nums: List[int]) -> int:
        zeros = [i for i,j in enumerate(nums) if j==0]
        p = 0
        max1s = 0
        # print(locals())
        if len(zeros)==len(nums):
            return 0
        elif len(zeros)<2:
            return len(nums)-1
        else:
            zeros = [-1] + zeros + [len(nums)]
        # print(locals())
        while p<len(zeros)-2:
            # print(locals())
            i, j, k = zeros[p:p+3]
            max1s = max(max1s, k-1-i-1)
            p += 1
            # print(locals())
        return max1s