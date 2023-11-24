# https://leetcode.com/problems/increasing-triplet-subsequence
# https://leetcode.com/problems/334-increasing-triplet-subsequence
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = []
        b = [0]*len(nums)
        prev = nums[0]
        s.append(prev)
        for i in nums[1:]:
            if i <prev:
                prev = i
            s.append(prev)
    
        j = len(nums)-1
        prev = nums[j]
        b[j] = nums[j]
        while j>-1:
            if nums[j]>prev:
                prev = nums[j]
            b[j] = prev
            j -= 1
        i = 0
        while i< len(nums):
            if s[i]<nums[i]<b[i]:
                return True
            i += 1
        return False



        