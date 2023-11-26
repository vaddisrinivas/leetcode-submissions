class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box= [[set() for i in range(3)] for j in range(3)]
        for row in range(9):
            rset = set()
            cset = set()
            for col in range(9):
                if board[row][col]!=".":
                    if board[row][col] in rset: return False
                    rset.add(board[row][col])
                if board[col][row]!=".":
                    if board[col][row] in cset or board[col][row] in box[col//3][row//3]: return False
                    cset.add(board[col][row])    
                    box[col//3][row//3].add(board[col][row])
        return True