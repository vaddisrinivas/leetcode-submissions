# https://leetcode.com/problems/isomorphic-strings
# https://leetcode.com/problems/205-isomorphic-strings
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        chars = {}
        if len(set(s))!=len(set(t)):
            return False
        for i in range(len(s)):
            if s[i] in chars:
                if t[i]!=chars[s[i]]:
                    return False
            else:
                chars[s[i]]=t[i]
        return True