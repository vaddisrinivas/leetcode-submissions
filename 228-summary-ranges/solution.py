class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums)==0: return []
        n,l,i,j,x = nums[-1],len(nums),nums[0],0,0
        res = []
        while j<l and i<n+1:
            if i!=nums[j]: 
                res.append(f"{nums[x]}->{nums[j-1]}"if x<j-1 else f"{nums[j-1]}")
                x = j
                i=nums[j]
            i,j = i+1,j+1
        res.append(f"{nums[x]}->{nums[j-1]}"if x<j-1 else f"{nums[j-1]}")
        return res