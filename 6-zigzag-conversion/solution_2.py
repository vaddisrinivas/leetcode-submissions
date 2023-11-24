# https://leetcode.com/problems/zigzag-conversion
# https://leetcode.com/problems/6-zigzag-conversion
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """        
        if numRows ==1:
            return s
        col = 0
        sol_dict = {i:[] for i in range(numRows)}
        row = 0
        c = 0
        while c < len(s):
            if row == numRows:
                while row-1>0 and c<len(s):
                    row-=1
                    col+=1
                    sol_dict[row-1].append(s[c])
                    c+=1
                continue
            sol_dict[row].append(s[c])
            row+=1
            c+=1 
        return "".join("".join(sol_dict[i]) for i in range(numRows))