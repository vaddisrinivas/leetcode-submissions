# https://leetcode.com/problems/max-consecutive-ones-iii
# https://leetcode.com/problems/1046-max-consecutive-ones-iii
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = [i for i, j in enumerate(nums) if j == 0]
        zeros = [-1] + zeros + [len(nums)]
        start, stop, maxcon = 1, 1, 0
        before, between = 0, 0

        if k == len(nums) or k>len(zeros):
            return len(nums)

        while stop < len(zeros):
            if (stop - start) == k:
                before, between = zeros[start] - zeros[start - 1], zeros[stop] - zeros[start] -1
                maxcon = max(maxcon, before + between)
                start += 1
            stop += 1
        return maxcon
