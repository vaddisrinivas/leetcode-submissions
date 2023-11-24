# https://leetcode.com/problems/jump-game-ii
# https://leetcode.com/problems/45-jump-game-ii
class Solution:
    def jump(self, nums: List[int]) -> int:

        l=len(nums)
        mins = [1]*l
        mins[-1]=0
        for i in range(l-2,-1,-1):
            if nums[i]==0: 
                mins[i]=0
                continue
            if nums[i]+i>=l-1: continue
            var = [mins[j] for j in range(i+1,i+nums[i]+1) if mins[j]!=0]
            if  var : mins[i]=1+min(var) 
            else: mins[i]=0
        return mins[0]
   