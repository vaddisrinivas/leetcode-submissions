# https://leetcode.com/problems/is-subsequence
# https://leetcode.com/problems/392-is-subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        i = 0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return True if i==len(s) else  False
        