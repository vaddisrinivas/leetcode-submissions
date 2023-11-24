# https://leetcode.com/problems/equal-row-and-column-pairs
# https://leetcode.com/problems/2428-equal-row-and-column-pairs
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
      cols = []
      for col_num in range(len(grid)):
        col = []
        for row in grid:
          col += [row[col_num]]
        cols += [col]
      pairs = 0
      for i in range(len(grid)):
        for j in grid:
          if j==cols[i]:
            pairs += 1
      return pairs
        
        