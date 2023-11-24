# https://leetcode.com/problems/intersection-of-two-arrays
# https://leetcode.com/problems/349-intersection-of-two-arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        return list(set([i for i in nums2  if i in nums1]))