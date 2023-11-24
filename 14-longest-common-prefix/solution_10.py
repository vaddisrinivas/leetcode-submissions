# https://leetcode.com/problems/longest-common-prefix
# https://leetcode.com/problems/14-longest-common-prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = min(strs,key=len)
        res = ""
        broken = False
        for i in range(len(l)):
            for j in range(len(strs)):
                if l[i]!=strs[j][i]:
                    broken=True
                    break
            if broken: return res
            res += l[i]
            
        return res