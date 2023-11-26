class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m,n,mn = len(matrix),len(matrix[0]),len(matrix)*len(matrix[0])
        d={"U":0,"D":m,"L":-1,"R":n}
        def getnext(direction,curr):
            nonlocal d
            if direction=="U" :
                if curr[0]-1==d["U"]: return "R",(curr[0],curr[1]+1)
                else: return "U",(curr[0]-1,curr[1])
            elif direction=="D" :
                if curr[0]+1==d["D"]: return "L",(curr[0],curr[1]-1)
                else: return "D",(curr[0]+1,curr[1])
            elif direction=="L" :
                if curr[1]-1==d["L"]: return "U",(curr[0]-1,curr[1])
                else: return "L",(curr[0],curr[1]-1)
            else :
                if curr[1]+1==d["R"]: return "D",(curr[0]+1,curr[1])
                else: return "R",(curr[0],curr[1]+1)
        pd,pc = "R",(0,0)
        l = []
        for i in range(mn):
            l.append(matrix[pc[0]][pc[1]])
            nd,nc = getnext(pd,pc)
            if nd!=pd: d[pd]=pc[0] if pd in "UD" else pc[1]
            pd,pc = nd,nc

        return l
            

            
            

