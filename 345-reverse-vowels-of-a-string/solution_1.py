# https://leetcode.com/problems/reverse-vowels-of-a-string
# https://leetcode.com/problems/345-reverse-vowels-of-a-string
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(list("aeiouAEIOU"))
        front, back = 0, len(s)-1
        ff, fb = False, False
        while front<back:
            ff = s[front] in vowels
            fb = s[back] in vowels
            if ff and fb:
                # swap
                s = s[:front]+s[back]+s[front+1:back]+s[front]+s[back+1:]
                ff, fb = False, False
                front += 1
                back -= 1
            elif ff and not fb:
                # move from back
                back -= 1
            elif not ff and fb:
                # move from front
                front += 1
            else:
                front += 1
                back -= 1
        return s