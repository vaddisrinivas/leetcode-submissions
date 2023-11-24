# https://leetcode.com/problems/valid-palindrome
# https://leetcode.com/problems/125-valid-palindrome
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n =""
        for i in s:
            if i.isalnum():n+=i.lower()
        s=n
        l=len(s)
        if l==1:
            return True
        elif l==2:
            return s[0]==s[1]
        elif l==3:
            return s[0]==s[2]
        if l%2==0:
            return s[:l//2]==s[l//2:][::-1]
        else:
            return s[:(l//2)-1]==s[(l//2)+2:][::-1]