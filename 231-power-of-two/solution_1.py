# https://leetcode.com/problems/power-of-two
# https://leetcode.com/problems/231-power-of-two
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        c = 0
        while n>0:
            print(n,n&1)
            if n&1:
                c+=1
            n = n >> 1
        return c==1