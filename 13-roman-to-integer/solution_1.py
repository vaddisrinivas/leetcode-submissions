# https://leetcode.com/problems/roman-to-integer
# https://leetcode.com/problems/13-roman-to-integer
class Solution:
    def romanToInt(self, s: str) -> int:
        c = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
        x = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i,l =len(s)-1,len(s)
        n = 0
        while i>-1:
            if s[i-1]+s[i] in c:
                n+=c[s[i-1]+s[i]]
                i-=2
            else:
                n+=x[s[i]]
                i-=1
            if i==0:
                n+=x[s[i]]
                break
        return n