class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)<2: return len(nums)
        nums = list(set(nums))
        nums.sort()
        prev,m,mm = nums[0],1,1
        for i in nums[1:]:
            if prev+1==i: m+=1
            else: 
                if mm<m: mm = m
                m = 1
            prev = i

        return max(mm,m)