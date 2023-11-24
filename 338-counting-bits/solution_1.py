# https://leetcode.com/problems/counting-bits
# https://leetcode.com/problems/338-counting-bits
class Solution:
    def countBits(self, n: int) -> List[int]:
        # 0 0 2**0
        # 1 1 
        # 1 0 2**1
        # 2 1
        # 1 0 2**2
        # 2 1 
        # 2 0
        # 3 1
        # 1 0 2**3
        # 2 1
        # 2 0
        # 3 1 
        # 2 0
        # 3 1
        # 3 0
        # 4 1
        # 1 0 2**4
        # FIRST HALF, FIRST HALF + 1
        if n==0:
            return [0]
        i = 2
        p = 0
        x = 0
        y = 0
        res = [0,1]
        while i < n+1:
            if i==2**(p+1):
                res.append(1)
                x = 1
                y = 0
                p += 1
            elif i < 2**p + 2**(p-1):
                res.append(res[2**(p-1)+x])
                x += 1
            else:
                res.append(res[2**(p-1)+y]+1)
                y += 1
            i += 1
        return res


