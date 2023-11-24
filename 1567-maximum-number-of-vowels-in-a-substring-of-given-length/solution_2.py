# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length
# https://leetcode.com/problems/1567-maximum-number-of-vowels-in-a-substring-of-given-length
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
      v = set(list("aeiou"))
      mv = sum([1 if i in v else 0 for i in s[:k]])
      cv = mv
      for i in range(1,len(s)-k+1):
        cv = cv-1 if s[i-1] in v else cv
        cv = cv+1 if s[i+k-1] in v else cv
        mv = mv if mv > cv else cv
      return mv

