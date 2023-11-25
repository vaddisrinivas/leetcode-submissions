class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for ind,i in enumerate(nums):
            if i not in s:
                s[i] = []
            s[i].append(ind)
        for ind,i in enumerate(nums):
            s[i].remove(ind)
            if target-i in s and len(s[target-i])>0: return [ind,s[target-i][0]]
            s[i].append(ind)
        return []