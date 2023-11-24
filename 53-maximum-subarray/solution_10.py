# https://leetcode.com/problems/maximum-subarray
# https://leetcode.com/problems/53-maximum-subarray
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = -1000000
        max_ending_here = 0

        for rating in nums:
            max_ending_here = max_ending_here + rating
            if max_ending_here < rating:
                max_ending_here = rating
            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
        return max_so_far