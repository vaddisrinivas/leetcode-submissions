# https://leetcode.com/problems/string-compression
# https://leetcode.com/problems/443-string-compression
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        if len(chars)==1:
            return 1
        s = ""
        i = 1
        temp = chars[0]
        prev = 1
        while i<len(chars):
            if chars[i]==temp:
                prev += 1
            else:
                s += temp+(str(prev) if prev>1 else "")
                temp = chars[i]
                prev = 1
            i += 1
        s += temp+(str(prev) if prev>1 else "")
        # print(s)
        for i in range(len(s)):
            chars[i]=s[i]
        return len(s)               
