# https://leetcode.com/problems/reverse-words-in-a-string
# https://leetcode.com/problems/151-reverse-words-in-a-string
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = ""
        for j in ([i for i in s.strip().split(" ")][::-1]):
            if len(j)==0:
                continue
            r += j+" "
        return r.strip()