# https://leetcode.com/problems/unique-paths
# https://leetcode.com/problems/62-unique-paths
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        c = [0]*n
        g = [c]*m
        g[-1] = [1]*n
        if m<2:
            return 1
        for i in range(m):
            g[i][-1]=1
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                g[i][j] = g[i+1][j]+g[i][j+1]
                
        return g[0][0]



