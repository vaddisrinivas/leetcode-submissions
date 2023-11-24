# https://leetcode.com/problems/find-the-difference-of-two-arrays
# https://leetcode.com/problems/1392-find-the-difference-of-two-arrays
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a = set(nums1)
        b = set(nums2)
        return [a.difference(b),b.difference(a)]
        