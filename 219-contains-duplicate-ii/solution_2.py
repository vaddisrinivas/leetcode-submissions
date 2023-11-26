class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for ind,i in enumerate(nums):
            if i in d and  ind-d[i]<=k: return True
            d[i]=ind
        return False