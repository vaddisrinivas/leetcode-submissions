# https://leetcode.com/problems/first-bad-version
# https://leetcode.com/problems/278-first-bad-version
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        stop = n
        mid = (start+stop)//2
        while start<stop:
            # print(start, stop, mid)
            if isBadVersion(mid):
                stop = mid
            else:
                start = mid + 1
            mid = (start+stop)//2
        return stop
