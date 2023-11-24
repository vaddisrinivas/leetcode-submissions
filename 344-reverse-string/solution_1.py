# https://leetcode.com/problems/reverse-string
# https://leetcode.com/problems/344-reverse-string
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = len(s)
        for i in range(l//2):
            s[i],s[l-1-i]=s[l-1-i],s[i]
            print( s[i],s[l-1-i])