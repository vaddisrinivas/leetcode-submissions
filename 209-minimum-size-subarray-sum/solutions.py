class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        for i in nums:
            if i>=target: return 1
        if sum(nums)<target: return 0
        i,l,s,j,m  = 0,len(nums),0,0,len(nums)
        while i<l:
            s += nums[i]
            if s>=target:
                while s>=target: s,j=s-nums[j],j+1
                m = min(i-j+2,m)
            i+=1
        return m 