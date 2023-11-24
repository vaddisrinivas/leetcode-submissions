# https://leetcode.com/problems/decode-string
# https://leetcode.com/problems/394-decode-string
class Solution:
    def decodeString(self, s: str) -> str:
        st = []
        res = ""
        i = 0
        dig = ""
        while i < len(s):
            if s[i].isdigit():
                dig += s[i]
            elif s[i].isalpha():
                if len(st)==0:
                    res += s[i]
                else:
                    st[0][1]+= s[i]
            elif s[i]=="[":
                st = [[int(dig),""]]+st
                dig = ""
            elif s[i]=="]":
                if len(st)==1:
                    res += st[0][0]*st[0][1]
                    st = []
                else:
                    st[1][1] += st[0][0]*st[0][1]
                    del st[0]
            i += 1
        return res






            
                
                
                



