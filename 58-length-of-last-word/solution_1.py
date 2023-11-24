# https://leetcode.com/problems/length-of-last-word
# https://leetcode.com/problems/58-length-of-last-word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c = 0
        w = False
        for i in range(len(s)-1,-1,-1):
            if s[i]==" ":
                if w: break
            else:
                c += 1
                w = True
        return c