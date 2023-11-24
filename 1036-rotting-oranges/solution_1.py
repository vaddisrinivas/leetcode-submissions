# https://leetcode.com/problems/rotting-oranges
# https://leetcode.com/problems/1036-rotting-oranges
from queue import Queue
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        mins = 0
        d = Queue()
        fo = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]==2:
                    d.put((i,j,0))
                elif grid[i][j]==1:
                    fo += 1
        m = set()
        twos = d.qsize()
        if fo==0:
            return 0
        while d.qsize()>0:
            i, j, k = d.get()
            r, c = len(grid),len(grid[i])
            # print(i,j,k,m,c)
            if grid[i][j]==1:
                grid[i][j]=2
                fo -= 1
            if i+1<r and 0<=j<c and grid[i+1][j]==1 and (i+1,j) not in m:
                d.put((i+1,j,k+1))
                m.add((i+1,j))
            if i-1>=0 and 0<=j<c and grid[i-1][j]==1  and (i-1,j) not in m:
                d.put((i-1,j,k+1))
                m.add((i-1,j))

            if 0<=i<r and j+1<c and grid[i][j+1]==1 and (i,j+1) not in m:
                d.put((i,j+1,k+1))
                m.add((i,j+1))

            if 0<=i<r and j-1 >=0 and grid[i][j-1]==1 and (i,j-1) not in m:
                d.put((i,j-1,k+1))
                m.add((i,j-1))

        return k if not fo else -1

                   
                   
         