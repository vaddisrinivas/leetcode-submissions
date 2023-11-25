class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s)!=len(pattern): return False
        ds, dt = {},{}
        for ind in range(len(s)):
            if s[ind] not in ds:
                ds[s[ind]]=pattern[ind]
            if pattern[ind] not in dt:
                dt[pattern[ind]]=s[ind]
            if s[ind]!=dt[pattern[ind]] or pattern[ind]!=ds[s[ind]]: return False 
        return True