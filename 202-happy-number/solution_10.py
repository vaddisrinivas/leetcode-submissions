# https://leetcode.com/problems/happy-number
# https://leetcode.com/problems/202-happy-number
class Solution:
    def isHappy(self, n: int) -> bool:
        def sos(n):
            return sum([int(i)**2 for i in str(n)])
        
        slow, fast = n, sos(sos(n))

        while (slow != fast) and (fast != 1):
            # print(slow, fast)
            slow, fast = sos(slow),sos(sos(fast))
            # print(slow, fast)
        return fast == 1