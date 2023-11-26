class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix)==1: return 
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
        pd,pc,ndc,replace = "R",(0,0),0,False
        l = []
        for i in range(mn+1):
            l.append(matrix[pc[0]][pc[1]])
            nd,nc = getnext(pd,pc)
            
            if nd!=pd: 
                d[pd]=pc[0] if pd in "UD" else pc[1]
                ndc += 1
                replace = True
                
            if replace:
                matrix[pc[0]][pc[1]]=l.pop(0)
            if ndc and ndc%4==0: 
                for j in range(pc[1],d["R"]):
                    matrix[pc[0]-1][j]=l.pop(0)
                ndc = 0
                replace = False
            pd,pc = nd,nc

        return l
            

