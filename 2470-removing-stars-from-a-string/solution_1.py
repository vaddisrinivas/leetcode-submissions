# https://leetcode.com/problems/removing-stars-from-a-string
# https://leetcode.com/problems/2470-removing-stars-from-a-string
class Solution:
    def removeStars(self, s: str) -> str:
        star = '*'
        ind = 0
        c = 0
        while ind<len(s):
            if s[ind]==star:
                s = s[:ind-1]+s[ind+1:]
                ind -=1
                continue
            ind += 1
        return s