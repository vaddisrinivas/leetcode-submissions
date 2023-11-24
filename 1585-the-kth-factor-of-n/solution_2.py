# https://leetcode.com/problems/the-kth-factor-of-n
# https://leetcode.com/problems/1585-the-kth-factor-of-n
12
# 1 3 5 6 4 2
# 1 2 3 4 6 12
# 1,2,3,4,6,12

import math
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        f = 0
        x = []
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                x.append(i)
                if i!=n//i:
                    x.append(n//i)            
        x.sort()
        return x[k-1] if k <=len(x) else -1