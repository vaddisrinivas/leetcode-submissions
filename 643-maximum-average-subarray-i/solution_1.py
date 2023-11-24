# https://leetcode.com/problems/maximum-average-subarray-i
# https://leetcode.com/problems/643-maximum-average-subarray-i
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        avg = sum(nums[:k])
        prev = sum(nums[:k])
        for i in range(1,len(nums)-k+1):
            prev = prev-nums[i-1]+nums[i+k-1]
            avg = max(avg,prev)
        return avg/k