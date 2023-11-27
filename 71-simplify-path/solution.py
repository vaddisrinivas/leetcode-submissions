class Solution:
    def simplifyPath(self, path: str) -> str:
        if path[-1]!="/": path+="/"
        i,prev,l,st = 0,0, len(path),[]
        while i<l:
            if path[i]=="/":
                st.append()
                prev = i+1
            i+=1
        st.append(path[prev:-1])
        res = ""
        skips = 0
        i = len(st)-1
        while i>-1:
            if st[i]=="" or st[i]==".": None
            elif st[i]=="..": skips +=1
            else:
                if skips==0: res = "/"+st[i]+res
                if skips>0: skips -=1
            i-=1
        return res if res else "/"