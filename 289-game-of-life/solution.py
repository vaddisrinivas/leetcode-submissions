class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m,n,d = len(board), len(board[0]),{}
        def lives(r,c):
            nonlocal m,n,d
            x,delta = 0, board[r][c]
            rm, mr, cm, mc = r-1,r+2,c-1,c+2
            if c==n-1: mc = c+1
            if c==0: cm = 0
            if r==m-1: mr = r+1
            if r==0: rm = 0
            # print(rm,mr,cm,mc)
            for i in range(rm,mr):
                for j in range(cm,mc):
                    # print(i,j,x,d)
                    if (i,j) in d: x+=d[(i,j)]
                    else:
                        x+=board[i][j]
            x-=delta 
            if delta:  return True if (x==2 or x==3) else False
            else: return True if x==3 else False
        for i in range(m):
            for j in range(n):
                l = lives(i,j)
                # print(l,i,j)
                if (l and not board[i][j]) or (not l and board[i][j]):
                    d[(i,j)]=board[i][j]
                    # print("change",(i,j),d[(i,j)]) 
                    board[i][j]= 0 if board[i][j] else 1
                 
                