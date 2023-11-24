# https://leetcode.com/problems/reverse-words-in-a-string-iii
# https://leetcode.com/problems/557-reverse-words-in-a-string-iii
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        res = ""
        for i in words:
            res += i[::-1]
            res += " "
        return res.strip()