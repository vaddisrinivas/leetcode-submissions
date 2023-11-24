# https://leetcode.com/problems/number-of-islands
# https://leetcode.com/problems/200-number-of-islands
class Solution:
    def numIslands(self, grid: List[List[str]]):
        eq ={}
        s = set()
        h = 0
        i,j=0, 0
        x,y = len(grid), len(grid[0])
        def valid(k):
            p,q = k
            nonlocal s
            if 0<=p<x and 0<=q<y and grid[p][q]=="1" and (p,q) not in s:
                return True
            else:
                return False
        c = 0
        for a in range(x):
            for b in range(y):
                if valid((a,b)):
                    eq[h] = (a,b)
                    s.add(eq[h])
                    t = h+1
                    while h<len(eq):
                        (i,j) = eq[h]
                        s.add(eq[h])
                        for k in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                            if valid(k):
                                # print("valid",k,h,t,eq)
                                eq[t] = k
                                t += 1
                                grid[k[0]][k[1]] = 0
                            # else:
                            #     print("invalid",k)
                        h+=1
                    h = t
                    c += 1
        return c


                        
            
