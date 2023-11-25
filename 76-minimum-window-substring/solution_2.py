class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lt, ls= len(t), len(s)
        if lt>ls: return ""
        td, sd, j, x = Counter(t), Counter(s), 0, (0,ls)
        if lt==ls: return s if sd==td else ""
        def isokay(d,t):
            for i in t:
                if i not in d: return False
                if t[i]>d[i]: return False
            return True
        if not isokay(sd,td): return ""
        dummy = {k:0 for k in td}        
        for i in range(len(s)):
            if s[i] in dummy: 
                dummy[s[i]]+=1
            while isokay(dummy,td):
                if i+1-j<=x[1]-x[0]: 
                    x = (j,i+1)
                if s[j] in dummy: dummy[s[j]]-=1
                j+=1
        return s[x[0]:x[1]] 