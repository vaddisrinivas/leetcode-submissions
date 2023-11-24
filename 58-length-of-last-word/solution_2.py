# https://leetcode.com/problems/length-of-last-word
# https://leetcode.com/problems/58-length-of-last-word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c = 0
        for i in range(len(s)-1,-1,-1):
            if s[i]==" ":
                if c: break
            else:
                c += 1
        return c