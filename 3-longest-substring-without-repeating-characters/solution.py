class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j,l,r,m = 0,0,len(s),set(),0
        for i in range(l):
            while s[i] in r:
                r.remove(s[j])
                j+=1
            r.add(s[i])
            if len(r)>m: m = len(r)
        return m
                