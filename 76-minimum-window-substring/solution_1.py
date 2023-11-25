class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lt, ls= len(t), len(s)
        if lt>ls: return ""
        td, sd, j, x = Counter(t), Counter(s), 0, (0,ls+1)
        if lt==ls: return s if sd==td else ""
        def isokay(d,t):
            for i in t:
                if i not in d or t[i]>d[i]: return False
            return True
        if not isokay(sd,td): return ""
        dummy = {k:0 for k in td}
        ts = None
        i=0
        while i<ls:
            if s[i] in td:
                break
            i += 1
        q = i
        ch = s[q]
        for i in range(q,ls):
            if s[i] in dummy: dummy[s[i]]+=1
            if isokay(dummy,td):
                x = (q,i+1)
                break
        p = i
        while True:
            if s[q] not in dummy: 
                q+=1
                continue
            if i+1-q<x[1]-x[0]:
                x=(q,i+1)
            
            dummy[s[q]]-=1
            if dummy[s[q]]<td[s[q]]:
                ch=s[q]
                q+=1
                break
            q+=1
        for i in range(p+1,len(s)):
            if s[i] in dummy: dummy[s[i]]+=1 
            if s[i]==ch:
                while True:
                    if s[q] not in dummy: 
                        q+=1
                        continue
                    if i+1-q<x[1]-x[0]:
                        x=(q,i+1)
                    
                    dummy[s[q]]-=1
                    if dummy[s[q]]<td[s[q]]:
                        ch=s[q]
                        q+=1
                        break
                    q+=1
        return s[x[0]:x[1]] if x!=(0,ls+1) else ""