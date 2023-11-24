# https://leetcode.com/problems/guess-number-higher-or-lower
# https://leetcode.com/problems/374-guess-number-higher-or-lower
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int,) -> int:
        l, r = 0, n
        while l<=r:
            i = (l+r)//2
            g = guess(i)
            if g == -1:
                r = i
            elif g == 1:
                l = i+1
            else:
                return i
        return 1
        