# https://leetcode.com/problems/flood-fill
# https://leetcode.com/problems/733-flood-fill
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        try:
            m = len(image)
            n = len(image[0])
        except:
            return [[]]*m
        if sr>m and sc>n:
            return image
        target = image[sr][sc]
        stack = []
        visited = {(i,j):False for j in range(n) for i in range(m)}
        i = sr
        j = sc

        def change(i,j):
            print("in change",i,j)
            visited[(i,j)]=True
            if image[i][j]==target:
                image[i][j]=color
                return True
            else:
                return False
        
        def dfs(i,j):
            print("in dfs",i,j)
            if i>=m or j>=n:
                return False
            if i<0 or j<0:
                return False
            if visited[(i,j)]:
                return False            
            stack.append((i,j))
            if change(i,j):
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
                stack.pop()
            return 
        dfs(i,j)
        return image