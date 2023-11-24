# https://leetcode.com/problems/combination-sum-iii
# https://leetcode.com/problems/216-combination-sum-iii
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        def bt(curr,curr_pos,st,s):
            if curr_pos==k-1:
                if st<=n-s<=9:
                    result.append(curr+[n-s])
                return
            for i in range(st,10):
                if i>=n-s:
                    continue
                bt(curr + [i],curr_pos+1,i+1,s+i)
        bt([],0,1,0)
        return result